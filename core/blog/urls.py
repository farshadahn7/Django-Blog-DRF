from django.urls import path, include
from rest_framework.urls import app_name

app_name = "blog"

urlpatterns = [
    path("api/v1/", include("blog.api.v1.urls")),
]
