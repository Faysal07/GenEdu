from django.db  import models

from subjects.models import Subject

# Create your models here.


# Teacher Model Here
class Teacher(models.Model):
    TECHER_TYPE = (
        ('teacher', 'Teacher'),    
        ('assistant', 'Assistant'),
    )
    
    teacherSerial = models.IntegerField()
    teacherId = models.IntegerField()
    teacherName = models.CharField(max_length=100)
    teacherCardNo = models.IntegerField(unique=True)
    teacherDesignation = models.CharField(max_length=100)
    teacherInfo = models.TextField()
    teacherSubject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacherCategory = models.CharField(max_length=20, choices=TECHER_TYPE)
    teacherEmail = models.CharField(unique=True)
    teacherCreated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.teacherName
    