from django.urls import path
from . import views

urlpatterns = [
    path("cars/", views.CarList.as_view()),
    path("cars/<int:pk>", views.CarDetail.as_view()),
    path("customers/", views.CustomerList.as_view()),
    path("appointments/", views.AgendaList.as_view()),
]