from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.shortcuts import get_object_or_404

from .serializers import PostSerializers
from ...models import Post


class PostsView(ListAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()


class PostDetailsView(RetrieveAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()

    def get_object(self):
        slug = self.kwargs["slug"]
        year = self.kwargs["year"]
        month = self.kwargs["month"]
        day = self.kwargs["day"]
        obj = get_object_or_404(self.queryset, slug=slug, published_date__year=year, published_date__month=month,
                                published_date__day=day)
        return obj
