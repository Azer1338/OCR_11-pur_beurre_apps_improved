from django.conf.urls import url

from . import views
# import views so we can use them in urls.py.

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.signup_view, name="signup"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^myAccount/$', views.my_account_view, name="myAccount"),
]
