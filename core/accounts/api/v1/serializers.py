from typing import Any

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

from ...models import CustomUser, Profile
from .pass_validator import pass_validator


class RegistrationSerializers(serializers.ModelSerializer):
    re_password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 're_password']

    def validate(self, attrs):
        pass_validator(attrs.get('password'), attrs.get('re_password'))
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop('re_password')
        user = CustomUser.objects.create_user(**validated_data)
        user.save()
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['email'] = self.user.email
        data['username'] = self.user.username
        data['id'] = self.user.id
        return data


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    pass


class ChangePasswordSerializers(serializers.ModelSerializer):
    re_password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['password', 're_password']

    def validate(self, attrs):
        pass_validator(attrs.get('password'), attrs.get('re_password'))
        return super().validate(attrs)

    def update(self, instance, validated_data):
        validated_data.pop("re_password")
        if instance.check_password(validated_data.get("password")):
            raise serializers.ValidationError("Password cannot be equal to the previous one.")
        else:
            instance.set_password(validated_data.get("password"))
            instance.save()
            return instance


class ForgetPasswordEmailSerializers(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = CustomUser
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get("email")
        if not CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({"details": "There is no email registered before."})
        return super().validate(attrs)


class ResetPasswordSerializers(serializers.ModelSerializer):
    re_password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['password', 're_password']

    def validate(self, attrs):
        pass_validator(attrs.get('password'), attrs.get('re_password'))
        return super().validate(attrs)

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'bio', 'avatar']



