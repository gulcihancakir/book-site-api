from django.urls import path
from . import views

urlpatterns = [
    path('quotation', views.QuotationView.as_view()),
    path('quotation/add', views.QuotationPostView.as_view()),
   
]