from django.conf.urls import url

from . import views
# import views so we can use them in urls.py.

app_name = 'main'

urlpatterns = [
    url(r'^$', views.index_view, name="index"),
    url(r'^mentions/$', views.mentions_view, name="mentions"),
]
