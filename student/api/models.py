from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'student'

class Subject(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='subjects')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'subject'