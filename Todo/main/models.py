from django.db import models

# Create your models here.

class Todo(models.Model):

    # gradechoices = [
    #       ('A+','100'), 
    #       ('B+','85'),
    #       ('C+','60'),
    # ]

    # grades = models.CharField(max_length=2, choices=gradechoices , null=True , blank=True)
    # describtion = models.TextField()    
    name = models.CharField(max_length=100 )
    createdAt = models.DateTimeField(auto_now_add= True , null=True, blank=True )  # search for auto-now-add
    is_Completed = models.BooleanField(default=False)


    def __str__(self):

        return self.name
    

    



class TodoItems(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    Describtion = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True , null=True , blank=True)
    is_Completed = models.BooleanField(default=False)
    todo = models.ForeignKey(Todo, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):

        return self.name
    



