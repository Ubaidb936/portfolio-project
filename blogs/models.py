from django.db import models

class Blog(models.Model):
    title = models.TextField(max_length = 255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')
