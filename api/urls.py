from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginUser.as_view()),
    path('register/', views.RegisterUser.as_view()),
    path('profile/', views.FetchUserProfile.as_view())
]
