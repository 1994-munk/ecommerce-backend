from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(["GET"])
def get_categories(request):
    return Response({"message": "Categories endpoint working"})
