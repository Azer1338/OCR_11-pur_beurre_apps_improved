from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect

from pur_beurre_project.settings import API_GOOGLE_KEY
from .models import Aliment, UserLinkToAlimentsTable


def search_view(request):
    """
    Display a list of similar aliments based on user's query.
    :param request: User's request
    :return:
    """
    # Initiate some variables
    # Generate a dictionary to collect user'choices
    nutriscore_wished_list = []
    # List the checkboxes in the template
    nutriscore_dict = {'nutriscore_a': 'a',
                       'nutriscore_b': 'b',
                       'nutriscore_c': 'c',
                       'nutriscore_d': 'd',
                       'nutriscore_e': 'e'
                       }
    # List of aliment
    aliment_list = []
    # Context
    check_box_choices = ""

    # Collect the User's request
    query = request.GET.get('userSearch')

    # Collect the User's choices
    for key, values in nutriscore_dict.items():
        if request.GET.get(key):
            nutriscore_wished_list.append(values)
            # Add user'choices in the context
            check_box_choices = check_box_choices + key + "=on&"
    # If no checkboxes checked, all checkboxes are checked
    if not nutriscore_wished_list:
        nutriscore_wished_list.extend(['a',
                                       'b',
                                       'c',
                                       'd',
                                       'e'])
        check_box_choices = 'nutriscore_a=on&nutriscore_b=on&nutriscore_c=on&nutriscore_d=on&nutriscore_e=on&'

    # Ensure that the query is filled
    if query:
        # Gather a list from database
        aliment_name = Aliment.objects.filter(name__icontains=query)
        # Check if we find some elements
        if not aliment_name.exists():
            # No result found message
            message = "Misère de misère, nous n'avons trouvé aucun résultat !"
        else:
            # Look for similar aliment
            message = "Vous pouvez remplacer cet aliment par:"
            # Collect a list of aliment with the same categories
            for elt in nutriscore_wished_list:
                search = Aliment.objects.filter(category__icontains=aliment_name[0].category,
                                                nutrition_score__icontains=elt).order_by('nutrition_score')
                aliment_list.extend(search)

    else:
        # No query send
        message = "Vous n'avez pas spécifié votre recherche. Voici notre liste."
        for elt in nutriscore_wished_list:
            search = Aliment.objects.filter(nutrition_score__icontains=elt).order_by('nutrition_score')
            aliment_list.extend(search)

    # Slice page
    paginator = Paginator(aliment_list, 6)
    # Get the current page
    page_number = request.GET.get('page')

    pag_obj = paginator.get_page(page_number)

    # Build the context
    context = {
        'substitutes': pag_obj,

        'user_request': query,
        'check_boxes_status': check_box_choices,
        'message': message,

        'paginate': True,
    }

    return render(request, 'substitute/search.html', context)


def detail_view(request, aliment_code):
    """
    Display the details of an aliment.
    :param request:
    :param aliment_code:
    :return:
    """

    # Get the aliment from his id
    aliment = Aliment.objects.get(code=aliment_code)

    # Get user'information
    if request.user.is_authenticated:
        current_user = request.user

    # Create a dictionary to feed the HTML page
    context = {
        'aliment': aliment,
        'api_key': API_GOOGLE_KEY,
    }
    # Add user'information to the feed
    if request.user.is_authenticated:
        context.update({'user_city': current_user.address})

    return render(request, 'substitute/details.html', context)


def favorites_view(request):
    """
    Display only the favorites substitutes.
    :param request:
    :return:
    """
    favorite_list = 0

    # Ensure that an user is authentified
    if request.user.is_authenticated:
        # Gather a list from database
        favorites_id_list = UserLinkToAlimentsTable.objects.filter(user_id=request.user)
        # Check if we find some elements
        if not favorites_id_list.exists():
            # List is empty
            message = "Misère de misère, vous n'avez encore pas enregistrer de favoris !"
            # Empty list
            favorite_list = []
        else:
            # Some elements are in the list
            message = "Voici vos favoris"
            # Collect the aliments from the list
            favorite_list = []
            for elt in favorites_id_list:
                adrien = Aliment.objects.filter(id=elt.aliment_id).distinct()
                favorite_list.extend(adrien)

    else:
        # User is not identified
        message = "Vous devez etre identifié pour voir vos favoris"

    # Slice page
    paginator = Paginator(favorite_list, 6)
    # Get the current page
    page = request.GET.get('page')

    # Return only this page substitute and not others
    try:
        favorite = paginator.page(page)
        print("Page OK")
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        favorite = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        favorite = paginator.page(paginator.num_pages)

    # Build the context
    context = {
        'substitutes': favorite,
        'message': message,
        'paginate': True,
    }

    return render(request, 'substitute/favorite.html', context)


def save_view(request, aliment_id):
    """
    Save the aliment selected as favorite in the database
    :param request:
    :param aliment_id:
    :return:
    """

    # Add the favorite aliment in the table
    UserLinkToAlimentsTable.objects.create(user_id=request.user, aliment_id=aliment_id)

    messages.success(request, 'Aliment ajouté!')

    return redirect(request.META['HTTP_REFERER'])


def delete_view(request, aliment_id):
    """
    Remove the aliment selected as favorite in the database
    :param request:
    :param aliment_id:
    :return:
    """

    # Add the favorite aliment in the table
    UserLinkToAlimentsTable.objects.filter(user_id=request.user, aliment_id=aliment_id).delete()

    messages.success(request, 'Aliment retiré!')

    return redirect(request.META['HTTP_REFERER'])
