from django.urls import path
from users.views import RegisterApi

urlpatterns = [
      path('api/register', RegisterApi.as_view()),
]
    