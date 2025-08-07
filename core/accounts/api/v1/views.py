from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from mail_templated import send_mail
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from decouple import config
from django.shortcuts import get_object_or_404

from .serializers import RegistrationSerializers, CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer
from ...models import CustomUser
from .manually_token import get_tokens_for_user


class RegistrationView(CreateAPIView):
    serializer_class = RegistrationSerializers

    def post(self, request, *args, **kwargs):
        serialized_date = self.serializer_class(data=request.data)
        serialized_date.is_valid(raise_exception=True)
        serialized_date.save()
        user = CustomUser.objects.filter(username=serialized_date.data.get("username")).first()
        access_token = get_tokens_for_user(user)
        msg = {
            'access_token': access_token,
            'username': user.username,

        }
        send_mail(template_name="email/email_verification.tpl", from_email="farshad@test.com", context=msg,
                  recipient_list=[user.email])
        return Response("Registration is done successfully. Please check your mail.", status=status.HTTP_201_CREATED)


class TokenJwtView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class TokenRefreshJwtView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer


class VerifyAccountView(APIView):
    def get(self, request, token, *args, **kwargs):
        try:
            user_data = jwt.decode(token, config("SECRET_KEY"), algorithms=["HS256"])
            print(user_data)
            user_obj = get_object_or_404(CustomUser, id=user_data["user_id"])
            user_obj.is_verified = True
            user_obj.save()
            return Response("Account verified successfully.", status=status.HTTP_200_OK)
        except ExpiredSignatureError as e:
            return Response({"details": e}, status=status.HTTP_400_BAD_REQUEST)
        except InvalidTokenError as e:
            return Response({"details": e}, status=status.HTTP_400_BAD_REQUEST)
