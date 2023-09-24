from django.db import models
from django.contrib.auth.models import User

class filesupload(models.Model):
    file=models.FileField()
    uploadedon=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
