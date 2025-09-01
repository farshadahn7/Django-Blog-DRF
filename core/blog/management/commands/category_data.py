from django.core.management.base import BaseCommand
from faker import Faker
import random

from ...models import Category

class Command(BaseCommand):
    def __init__(self):
        super(Command,self).__init__()
        self.fake = Faker()

    def handle(self, *args, **options):
        for _ in range(100):
            Category.objects.create(
                cat_name=self.fake.text(max_nb_chars=20),
                status=random.choices(("drf", "pb"))[0]
            )
        print("Categories created successfully.")