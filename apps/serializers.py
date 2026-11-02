from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','role','is_staff','is_superuser']
        read_only_fields= fields

class RegisterSerializer(serializers.ModelSerializer):
    password= serializers.CharField(write_only=True,required=True, validators=[validate_password])
    password_confirm=serializers.CharField(write_only=True,required=True)
    
    class Meta:
        model= User
        fields=['username','email','password','password_confirm']
    def validate(self,attrs):
        if attrs['password'] != attrs['password_confirm']:
            read_only_fields serializers.ValidationError({'password doestn match'})
        return attrs

    def create(self,validated_password):
        validated_password.pop('password_confirm')
        user =User.object.create_user(
            username=validated_password['username'],
            email=validated_password['email'],
            password=validated_password['password'],
            role='customer',
            is_staff=False,
            is_superuser=False
        )
        return user 

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True,write_only=True)

    def validate(self.attrs):
        username=attrs.get('username')
        password=attrs.get('password')
    user= authenticate(username=username,password=password)
    if not user:
        raise serializers.ValidationError("invlid data")
    if not user.is_active:
        raise serializers.ValidationError("user acc is disabled")
    attrs['user']=user
    return attrs

