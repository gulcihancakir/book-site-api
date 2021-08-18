from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.ReadingListView.as_view()),
   
]