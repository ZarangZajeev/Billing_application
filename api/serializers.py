from django.contrib.auth.models import User

from rest_framework import serializers

from api.models import USerProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email","password"]
        read_only_fields=["id"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = USerProfile
        fields = ["shop_name", "phone", "logo","user"]
        read_only_fields = ["id"]