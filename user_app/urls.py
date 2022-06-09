from django.urls import path
from knox import views as knox_views
from rest_framework.authtoken.views import obtain_auth_token

from user_app import views

from .views import RegisterAPI

app_name = "user_app"

urlpatterns = [
    path("login/", obtain_auth_token, name="login"),
    path("register/", RegisterAPI.as_view(), name="register"),
    path("logout/", views.logout_view, name="logout")
    # path('register/',views.registration_view,name='register')
]
