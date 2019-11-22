from django.db import models
from django.contrib.auth.models import User

class ToDo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    STATUS_CHOICES = [
        ("TODO", "To Do"),
        ("DOING", "Doing"),
        ("DONE", "Done"),
        ("BACKLOG", "Backlog")
    ]
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default="TODO")
    PRIORITY_CHOICES = [
        (0, "No Priority"),
        (1,"Low"),
        (2,"High"),
        (3,"Urgent")
    ]
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=0)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, default=None, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title