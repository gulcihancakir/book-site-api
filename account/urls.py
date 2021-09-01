from django.urls import path
from . import views

urlpatterns = [
    path('register', views.UserRegisterView.as_view()),    
    path('detail-reading-list/<int:pk>', views.UserReadingListView.as_view()),    
    path('detail-reads-list/<int:pk>', views.UserReadsListView.as_view()),    
    path('detail/<str:username>', views.UserSearchView.as_view()),    
]