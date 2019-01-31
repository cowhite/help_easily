from django.db import models
from django.contrib.auth.models import User

from utils.models import DateTimeBase


class Post(DateTimeBase):
    POST_TYPE_CHOICE_PEOPLE = 1
    POST_TYPE_CHOICE_ANIMALS = 2

    POST_TYPE_CHOICES = (
        (POST_TYPE_CHOICE_PEOPLE, 'People'),
        (POST_TYPE_CHOICE_ANIMALS, 'Animals'),
    )

    post_type = models.IntegerField(choices=POST_TYPE_CHOICES)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.content


class PostImage(DateTimeBase):
    image = models.ImageField(upload_to="post_images")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class PostVideo(DateTimeBase):
    file = models.FileField(upload_to="post_videos")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
