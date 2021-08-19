from django.urls import path
from . import views

urlpatterns = [
    path('account/register', views.UserRegisterView.as_view()),
    path('account/<int:pk>', views.UserDetailView.as_view()),
    
]