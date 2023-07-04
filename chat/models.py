import uuid
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Message(models.Model):
    body = models.TextField()
    sent_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='createdMessages', on_delete=models.SET_NULL, null=True)


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
