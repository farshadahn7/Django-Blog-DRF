from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model

from .serializers import PostSerializers, CategorySerializers, CategoryPostsSerializers
from ...models import Post, Category
from .permissions import IsOwnerOrReadOnly
from .tasks import send_email

CustomUser = get_user_model()


class PostsView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializers
    queryset = Post.objects.prefetch_related("category").filter(status="pb")

    def post(self, request, *args, **kwargs):
        created_post = super().post(request, *args, **kwargs)
        user = CustomUser.objects.filter(username=request.user).first()

        msg = {
            'username': user.username,
        }
        send_email.apply_async(
            kwargs={"template_name": "email/post_creation.tpl", "from_email": "farshad@test.com", "context": msg,
                    "recipient_list": [user.email]})
        return created_post


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


class CategoriesView(ListCreateAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()


class CategoryPostsView(RetrieveAPIView):
    serializer_class = CategoryPostsSerializers
    queryset = Category.objects.all()

    def get_object(self):
        slug = self.kwargs["slug"]
        obj = get_object_or_404(self.queryset, slug=slug)
        return obj
