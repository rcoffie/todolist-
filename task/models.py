from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task_owner")
    completed = models.BooleanField(default=False, blank=True, null=True)
    description = models.TextField()
    remark = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
