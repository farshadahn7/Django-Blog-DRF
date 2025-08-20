from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

User = get_user_model()


class Category(models.Model):
    class Status(models.TextChoices):
        Published = ("pb", "pub")
        Draft = ("drf", "draft")

    cat_name = models.CharField(max_length=128, unique=True)
    status = models.CharField(max_length=3, default=Status.Draft, choices=Status.choices)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, blank=True)


    def __str__(self):
        return self.cat_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.cat_name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:api-v1:category-detail", kwargs={"slug": self.slug})


class Post(models.Model):
    class Status(models.TextChoices):
        Published = ("pb", "pub")
        Draft = ("drf", "draft")

    title = models.CharField(max_length=256)
    content = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    status = models.CharField(max_length=3, default=Status.Draft, choices=Status.choices)
    post_image = models.ImageField(upload_to="post_images", null=True, blank=True)
    snippet = models.CharField(max_length=128, blank=True)
    category = models.ManyToManyField(Category, related_name="posts")

    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateField()
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if self.snippet == "":
            self.snippet = self.content[:128]
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:api-v1:post-details", kwargs={
            "slug": self.slug,
            "year": self.published_date.year,
            "month": self.published_date.month,
            "day": self.published_date.day,
        })

    class Meta:
        ordering = ["-published_date"]
        indexes = [
            models.Index(fields=["-published_date"])
        ]
        constraints = [
            models.UniqueConstraint(fields=['slug', 'published_date'], name='unique_slug_published_date')
        ]
