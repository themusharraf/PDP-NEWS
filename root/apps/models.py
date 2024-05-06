from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=225)
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    photo = models.ImageField(upload_to="images", blank=True, null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    subject = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name
