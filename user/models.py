from django.db import models
from datetime import datetime

class UserModel(models.Model):
    name = models.CharField(default = "", max_length = 25)
    surname = models.CharField(default = "", max_length = 25)
    about = models.TextField(default = "")
    yosh = models.IntegerField(default = 0)
    birth = models.DateTimeField(default = datetime.now())
    is_student = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.name

