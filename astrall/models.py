from django.db import models

class Photo(models.Model):
    file = models.FileField(upload_to='uploads/')