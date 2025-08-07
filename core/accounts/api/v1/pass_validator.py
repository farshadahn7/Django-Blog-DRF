from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

def pass_validator(first_password, second_password):
    if first_password != second_password:
        raise serializers.ValidationError({"details":"The passwords are not equal."})
    try:
        validate_password(first_password)
    except ValidationError as e:
        raise serializers.ValidationError({"details":list(e.messages)})