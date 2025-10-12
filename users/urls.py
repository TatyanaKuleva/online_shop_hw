from users.apps import UsersConfig
from django.urls import path
from django.contrib.auth.views import LoginView
from users.views import RegisterView


app_name = UsersConfig.name


urlpatterns = [
    path('login/', LoginView.as_view(template_name= 'login.html'), name='login'),
    path('register/',RegisterView.as_view(), name='register'),

]
