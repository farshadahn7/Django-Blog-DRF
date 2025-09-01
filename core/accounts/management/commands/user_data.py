import random

from django.core.management.base import BaseCommand
from faker import Faker
from django.db import IntegrityError
from ...models import CustomUser, Profile

class Command(BaseCommand):
    def __init__(self):
        super(Command, self).__init__()
        self.fake = Faker()

    def handle(self, *args, **options):
        for _ in range(5):
            try:
                user = CustomUser.objects.create_user(
                    username=self.fake.user_name(),
                    email=self.fake.email(),
                    password=self.fake.password(),
                    is_active=True,
                    is_verified= random.choices((True,False))[0],
                )
                user_profile = Profile.objects.filter(user=user).first()
                user_profile.first_name = self.fake.first_name()
                user_profile.last_name = self.fake.last_name()
                user_profile.bio = self.fake.text(max_nb_chars=10)
                user_profile.save()
            except IntegrityError:
                print("User already exists.")
                continue

        print("Users created successfully.")