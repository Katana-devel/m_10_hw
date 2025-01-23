from django.db import models
from django.contrib.auth.models import User  # Для связи с пользователем

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Quote(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    quote_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quotes')

    def __str__(self):
        return f'"{self.quote_text}" - {self.author.name}'
