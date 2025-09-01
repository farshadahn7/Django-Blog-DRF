import random

from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth import get_user_model
from ...models import Post, Category

User = get_user_model()


class Command(BaseCommand):
    def __init__(self):
        super(Command, self).__init__()
        self.fake = Faker()
        self.users = User.objects.all()
        self.cats = Category.objects.all()

    def handle(self, *args, **options):
        cats = self.cats
        cats_count = cats.count()
        user = self.users
        user_count = user.count()
        for _ in range(20):
            post = Post.objects.create(
                title=self.fake.text(max_nb_chars=20),
                content=self.fake.paragraph(nb_sentences=random.randint(5, 7)),
                author=user[random.choices(range(0, user_count))[0]],
                status=random.choices(("drf", "pb"))[0],
            )
            post.category.set([cats[random.choices(range(0, cats_count))[0]], cats[random.choices(range(0, cats_count))[0]]])

        print("Post Created successfully.")
