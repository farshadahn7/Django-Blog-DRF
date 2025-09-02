from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils.text import slugify

from ..models import Post, Category

User = get_user_model()

class TestPostModel(TestCase):
    def setUp(self):
        user_date = {
            "username":"test",
            "email":"test@test.com",
            "password":"123456@a",
            "is_verified":True
        }
        self.user = User.objects.create(**user_date)

        category_data = {
            "cat_name":"cat1",
            "status":"pub"
        }
        category_data_two = {
            "cat_name": "cat2",
            "status": "pub"
        }
        self.cat1 = Category.objects.create(**category_data)
        self.cat2 = Category.objects.create(**category_data_two)
        self.post_data = {
            "title":"test",
            "content":"this is test content",
            "author": self.user,
            "status":"pub",
        }


    def test_post_creation(self):
        post = Post.objects.create(**self.post_data)
        post.category.set([self.cat1,self.cat2])
        slug = slugify(post.title)
        self.assertEqual(post.title, self.post_data.get("title"))
        self.assertEqual(post.content, self.post_data.get("content"))
        self.assertEqual(post.author, self.post_data.get("author"))
        self.assertEqual(post.slug, slug)
        self.assertEqual(post.category.count(),2)
        self.assertIn(self.cat1, post.category.all())
        self.assertIn(self.cat2, post.category.all())
        self.assertTrue(isinstance(post, Post))

    def test_str_representation(self):
        post = Post.objects.create(**self.post_data)
        post.category.set([self.cat1, self.cat2])
        self.assertEqual(str(post), post.title)