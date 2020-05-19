from django.conf.urls import url
# import views so we can use them in urls.py.
from . import views


app_name = 'substitute'

urlpatterns = [
    url(r'^search/$', views.search_view, name="search"),
    url(r'^details/(?P<aliment_code>[0-9]+)/$',
        views.detail_view, name="detail"),
    url(r'^favorites/$', views.favorites_view, name="favorites"),

    url(r'^save/(?P<aliment_id>[0-9]+)/$', views.save_view, name="save"),
    url(r'^delete/(?P<aliment_id>[0-9]+)/$', views.delete_view, name="delete"),
]
