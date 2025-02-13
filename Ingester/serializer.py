from rest_framework import serializers
from .models import UserApi

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserApi
        fields = ['username', 'email', 'password']  # Add other fields as needed
        extra_kwargs = {'password': {'write_only': True}}  # Make password write-only

    def create(self, validated_data):
        user = UserApi(
            name=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])  # Use set_password to hash the password
        user.save()
        return user

