from django.db import models

# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' | ' + str(self.completed)
    
class Item(models.Model):
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    completed = models.BooleanField()

    def __str__(self):
        return self.text