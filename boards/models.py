from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_update = models.DateTimeField(auto_now_add=True)

    """ 
    models.ForeignKey(to, on_delete, **options) is a many-to-one relationship
    
    related_name creates a reverse relationship: each board instance will have access to 
    a list of Topic instances belonging to it
    """
    board = models.ForeignKey(
        Board, related_name="topics"
    )  # Topic has only 1 board instance
    starter = models.ForeignKey(User, related_name="topics")  # Topic has only 1 starter


class Post(models.Model):
    messsage = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name="posts")  # Post has only 1 topic

    # auto_now_add tells Django to set current date when Post object is created
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    # Post is created by 1 user
    created_by = models.ForeignKey(User, related_name="posts")

    # Post is only updated by 1 user at a time
    updated_by = models.ForeignKey(User, null=True, related_name="+")
