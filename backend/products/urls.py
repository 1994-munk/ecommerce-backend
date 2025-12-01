from django.urls import path
from . import views

urlpatterns = [
    # Example placeholder route
    path("", views.get_products, name="get_products"),
]
