from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class ToDoStatus(models.Model):
#     id = models.AutoField(primary_key=True)
#     status = models.CharField(max_length=255)

#     def __str__(self):
#         return self.status


# class ToDoPriority(models.Model):
#     id = models.AutoField(primary_key=True)
#     priority = models.CharField(max_length=255)

#     def __str__(self):
#         return self.priority

class ToDo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    # status = models.ForeignKey(ToDoStatus, on_delete=models.DO_NOTHING)
    # priority = models.ForeignKey(ToDoPriority, on_delete=models.DO_NOTHING)
    STATUS_CHOICES = [
        ("TODO", "To Do"),
        ("DOING", "Doing"),
        ("DONE", "Done"),
        ("BACKLOG", "Backlog")

    ]

    PRIORITY_CHOICES = [
        (0, "No Priority"),
        (1,"Low"),
        (2,"High"),
        (3,"Urgent")
    ]
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default="TODO")
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=0)
    # date_added = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, default=None, blank=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title