from django.db import models

# Create your models here.
class person(models.Model):
    name = models.CharField(max_length=50)
    event= models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    birth = models.DateTimeField()
    intro=models.TextField()
    elite=models.BooleanField(default=False)
    live=models.CharField(max_length=50)
    age=models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    def summary(self):
        return self.intro[:5]