from django.db import models


class LanguageChoices(models.TextChoices):
    PYTHON = 'py', 'Python'
    JAVASCRIPT = 'js', 'JavaScript'
    JAVA = 'java', 'Java'
    C = 'c', 'C'
    CPP = 'cpp', 'C++'
    OTHER = 'other', 'Other'

