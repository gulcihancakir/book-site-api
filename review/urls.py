from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view()),
    path('add', views.ReviewPostView.as_view()),
    path('detail/<int:pk>', views.ReviewDetailView.as_view()),
    path('update-delete/<int:pk>', views.ReviewUpdateDestroyView.as_view())
]