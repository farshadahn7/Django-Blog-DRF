from unicodedata import category

from django.template.context_processors import request
from rest_framework import serializers
from django.shortcuts import reverse
from ...models import Post, Category


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["cat_name", "slug"]
        read_only_fields = ("slug",)


class PostSerializers(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)
    category = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())
    post_details_link = serializers.SerializerMethodField(read_only=True)
    cat = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="blog:api-v1:category-detail",
        lookup_field='slug',
        source="category"
    )
    class Meta:
        model = Post
        fields = [
            "title",
            "snippet",
            "author",
            "post_image",
            "content",
            "status",
            "cat",
            "category",
            "published_date",
            "post_details_link",
        ]
        read_only_fields = ['snippet', "cat"]

    def get_post_details_link(self, instance):
        request = self.context.get("request")
        kwargs = {
            'slug': instance.slug,
            'year': instance.published_date.year,
            'month': instance.published_date.month,
            'day': instance.published_date.day
        }
        return request.build_absolute_uri(reverse("blog:api-v1:post-details", kwargs=kwargs))

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")
        if request.parser_context.get("kwargs").get("slug"):
            data.pop("snippet", None)
            data.pop("post_details_link", None)
        else:
            data.pop("content", None)
            data.pop("status", None)
        return data



