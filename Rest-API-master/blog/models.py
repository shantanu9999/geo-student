from django.db import models



class User(models.Model):
    name = models.CharField(max_length=120)
    dob = models.DateField()
   
    
    def __str__(self):
    	return self.name

