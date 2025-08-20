from rest_framework.response import Response
from django.utils.text import slugify
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .serializers import PostSerializers, CategorySerializers
from ...models import Post, Category
from .permissions import IsOwnerOrReadOnly


class PostsView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializers
    queryset = Post.objects.prefetch_related("category").filter(status="pb")


class PostDetailView(RetrieveUpdateAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.prefetch_related("category").all()
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        slug = self.kwargs["slug"]
        year = self.kwargs["year"]
        month = self.kwargs["month"]
        day = self.kwargs["day"]
        obj = get_object_or_404(self.queryset, slug=slug, published_date__year=year, published_date__month=month,
                                published_date__day=day)
        return obj


class CategoryDetails(RetrieveAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()

    def get_object(self):
        slug = self.kwargs["slug"]
        obj = get_object_or_404(self.queryset, slug=slug)
        return obj
