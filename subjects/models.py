from django.db import models

# My Creation models here.

# Subject Catagory Model Here


# Subject Model Here
class Subject(models.Model):
    SUBJ_CATAGORY = (
        ('science', 'Science'),
        ('commerce', 'Commerce'),
        ('arts', 'Arts'),
        ('alevel', 'A Level'),
        ('olevel', 'O Level'),
        ('general', 'General'),
    )
    
    subjectId = models.IntegerField()
    subjectName = models.CharField(max_length=50, unique=True)
    subjectCatagory = models.CharField(max_length=50, choices=SUBJ_CATAGORY)
    subjectCreated = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.subjectName
        

