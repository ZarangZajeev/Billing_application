from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions, authentication

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
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=UserProfileSerializer
    queryset=USerProfile.objects.all()

    def create(self, request, *args, **kwargs):
        raise serializers.ValidationError("Permission denied")
    
    def destroy(self, request, *args, **kwargs):
        raise serializers.ValidationError("Permission denied")
