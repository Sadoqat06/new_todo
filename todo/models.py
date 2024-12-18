from django.db import models
from datetime import datetime
from user.models import UserModel

class TodoModel(models.Model):
    text = models.TextField(default = "")
    deadline = models.DateTimeField(default = datetime.now())
    is_done = models.BooleanField(default = False)
    user = models.ForeignKey(UserModel, on_delete = models.CASCADE)
    
    def __str__(self) -> str:
        return self.text