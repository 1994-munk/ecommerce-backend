from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["GET"])
def get_products(request):
    return Response({"message": "Products endpoint working"})
