from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_signup_view, name='signup'),
    path('Login', views.user_login_view, name='login'),
    path('Logout', views.user_logout_view, name='logout'),
]