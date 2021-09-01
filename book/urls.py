from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view()),
    path('reading-post', views.ReadingPostView.as_view()),
    path('reads-post', views.ReadsPostView.as_view()),
    path('reading-delete/<int:pk>', views.ReadingListDeleteView.as_view()),
    path('reads-delete/<int:pk>', views.ReadsDeleteView.as_view()),
    path('search/<str:name>', views.BookSearchView.as_view()),    
    
]