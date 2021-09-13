from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuotationView.as_view()),
    path('add', views.QuotationPostView.as_view()),
    path('requotation-post', views.RequotationPostView.as_view()),
    path('requotation', views.RequotationView.as_view()),
    path('detail/<int:pk>', views.QuotationDetailView.as_view()),
    path('update-delete/<int:pk>', views.QuotationUpdateDestroyView.as_view()),
]