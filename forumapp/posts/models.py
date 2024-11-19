from django.db import models

from forumapp.posts.choices import LanguageChoices


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    languages = models.CharField(
        max_length=30,
        choices=LanguageChoices.choices,
        default=LanguageChoices.OTHER
    )
