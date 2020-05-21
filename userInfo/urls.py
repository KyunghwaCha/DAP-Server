from django.urls import path
from . import views

app_name = 'userInfo'
urlpatterns = [
    path('', views.UserView.as_view()),
    path('<str:userId>', views.UserView.as_view()),
]