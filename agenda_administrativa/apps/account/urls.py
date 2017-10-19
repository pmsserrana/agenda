from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    # post views
    # url(r'^login/$', views.user_login, name='login'),

    # login
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout_then_login'),


    # change password urls
    url(r'^password-change/$', auth_views.password_change, name='password_change'),
    url(r'^password-change/done/$', auth_views.password_change_done, name='password_change_done'),
]
