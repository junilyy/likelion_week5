from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
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
    a = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def summary(self):
        return self.intro[:5]