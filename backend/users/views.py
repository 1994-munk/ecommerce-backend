from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.permissions import AllowAny ,IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)
