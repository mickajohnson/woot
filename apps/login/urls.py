from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register$', views.register, name="register"),
    url(r'^login$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^users/edit/(?P<id>\d+)/$', views.edit_admin, name="edit_admin"),
    url(r'^users/show/update/(?P<id>\d+)/$', views.update, name="update"),
    url(r'^delete/user/(?P<id>\d+)$', views.delete_user, name="delete_user"),
    url(r'^users/edit/$', views.edit, name="edit"),
    url(r'^users/new/$', views.new, name="new"),
]
