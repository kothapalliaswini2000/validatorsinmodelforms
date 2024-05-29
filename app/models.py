from django.db import models
from django import forms
from django.core import validators

# Create your models here.

def validate_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('should not starts with a')

def validate_for_len(value):
    if len(value)>5:
        raise forms.ValidationError('lenght should be more than the 5')
    

    


class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True,validators=[validate_for_a,validate_for_len])
    

    def __str__(self):
        return self.topic_name
    

    
class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    email=models.EmailField(default='ashu@gmail.com')
    

    def __str__(self):
        return self.name
    
class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)

    def __str__(self):
        return self.author

