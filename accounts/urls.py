from django.conf.urls import url
# from django.contrib import admin
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
]
