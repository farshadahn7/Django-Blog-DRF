from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status
from .serializers import RegistrationSerializers


class RegistrationView(CreateAPIView):
    serializer_class = RegistrationSerializers

    def post(self, request, *args, **kwargs):
        serialized_date = self.serializer_class(data=request.data)
        serialized_date.is_valid(raise_exception=True)
        serialized_date.save()
        return Response("User is created successfully.", status=status.HTTP_201_CREATED)
