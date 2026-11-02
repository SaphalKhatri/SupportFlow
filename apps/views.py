from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import login,logout
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status,permissions
from rest_framework.views import APIView
from rest_framework.response import Response 
from .serializers import RegisterSerializer,LoginSerializer,UserSerializer
from django.middleware.csrf import get_token
# Create your views here.
class CSRFView(APIView):
    permissions_classes=[permissions.AllowAny]
    @ensure_csrf_cookie
    def get(self,requuest):
        return Response({
            "detail":"CSRF cookie set",
            "csrf_token":get_token(requuest)
        })

class RegisterView(APIView):
    permissions_classes=[permissions.AllowAny]

    def post(self,request):
        serializer =RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user= serializer.save()
            login(request,user)
            return Response(UserSerializer(user).data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def post(self,request):
        logout(request)
        return Response({"detial":"sucessfully logout"},status=status.HTTP_200_OK)

class CurrentUserView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request):
        serializer=UserSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)