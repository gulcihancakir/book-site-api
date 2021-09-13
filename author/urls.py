from django.urls import path
from . import views

urlpatterns = [
    path('', views.AuthorListView.as_view()),
    path('<int:pk>', views.AuthorDetailView.as_view()), 
    path('<str:fullname>', views.AuthorSearchView.as_view()),    

]