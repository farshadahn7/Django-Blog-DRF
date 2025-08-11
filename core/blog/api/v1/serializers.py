from rest_framework import serializers

from ...models import Category, Post


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'slug', 'status', 'snippet', 'published_date']