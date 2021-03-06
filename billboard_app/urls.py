from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_form, name='login'),
    url(r'^logout/$', views.logout_form, name='logout'),
]