from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions, authentication
from rest_framework import generics
from rest_framework.exceptions import ValidationError

from api.serializers import UserSerializer,UserProfileSerializer
from api.models import USerProfile


# Create your views here.
class SignUpView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Get the user instance
            # Automatically create user profile after successful user creation
            return Response(data=serializer.data)
        return Response(data=serializer.errors)

class UserProfileView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[JWTAuthentication]

    serializer_class = UserProfileSerializer
    queryset=USerProfile.objects.all()

    def get(self, request):
        user_profile =USerProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)