from django.shortcuts import render

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

    def perform_create(self, serializer):
        user_profile_exists = USerProfile.objects.filter(user=self.request.user).exists()
        if user_profile_exists:
            raise ValidationError("User profile already exists")
        serializer.save(user=self.request.user)