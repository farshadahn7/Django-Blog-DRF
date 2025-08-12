from django.urls import path

from . import views

app_name = "api-v1"

urlpatterns = [
    path("posts/", views.PostsView.as_view(), name="posts"),
    path("post/<slug:slug>/<str:year>/<str:month>/<str:day>/", views.PostDetailView.as_view(), name="post-details"),
    path("category/<slug:slug>/", views.CategoryDetails.as_view(), name="category-detail"),
]
