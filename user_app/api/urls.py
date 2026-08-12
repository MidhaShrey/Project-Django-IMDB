from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
]