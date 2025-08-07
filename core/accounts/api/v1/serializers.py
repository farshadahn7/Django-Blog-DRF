from rest_framework import serializers

from ...models import CustomUser
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