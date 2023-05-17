from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=255,default='name')
    email = models.EmailField(default='mmmm@mmm.com')
    age = models.IntegerField(default='22')
    address = models.CharField(max_length=255,default='mmm adress')

    
    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'Students Name'



class login(models.Model):
        username = models.CharField(max_length=50, null=True)
        password = models.CharField(max_length=50, null=True)