from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass  

class Circle(models.Model):
    name = models.CharField(max_length = 50)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="circles_created",
    )
    members = models.ManyToManyField(
        User,
        related_name="circles",
        blank=True
    )


class Task(models.Model):
    TODO = 'todo'
    DONE = 'done'

    STATUS_CHOICES = [
        (TODO, 'To Do'),
        (DONE, 'Done'),
    ]

    circle = models.ForeignKey(Circle, on_delete = models.CASCADE, related_name = "tasks")
    title = models.CharField(max_length = 50)
    desc = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "my_tasks")
    due_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=TODO)

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    circle = models.ForeignKey(Circle, on_delete = models.CASCADE, related_name='memberships')
    role = models.CharField(
    max_length = 20,
    choices = (('admin', 'Admin'), ('member', 'Member'),),
    default = 'member'
    )

    class Meta:
        unique_together = ('user', 'circle')