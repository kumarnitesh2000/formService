from django.db import models
from django.contrib.auth.models import User


class Form(models.Model):
    title = models.CharField(max_length=30,default='Untitled Form')
    description = models.TextField(max_length=250,default='Description Section')
    publishDate = models.DateTimeField(auto_now_add=True)
    endValidity = models.DateTimeField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'Title - {self.title}'


class Section(models.Model):
    sec_title = models.CharField(max_length=30, default='Untitled Section')
    description = models.TextField(max_length=250, default='Description Section')
    form = models.ForeignKey(Form,on_delete=models.CASCADE)

    def __str__(self):
        return f'Title - {self.sec_title}'


class Field(models.Model):
    CHOICE = (
        ('text', 'text'),
        ('choice', 'choice'),
        ('multipleChoices', 'multipleChoices'),
        ('datetime', 'datetime'),
        ('dropDown', 'dropDown'),
        ('fileUpload', 'fileUpload'),
        ('number', 'number')
    )
    description = models.CharField(max_length=50,default='Fill This')
    label = models.CharField(max_length=50,default='Label')
    required = models.BooleanField(default=False)
    field = models.TextField(choices=CHOICE)
    section = models.ForeignKey(Section,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f'Field Description - {self.description}'


class Choice(models.Model):
    option = models.CharField(max_length=50)
    field = models.ForeignKey(Field,on_delete=models.CASCADE)

    def __str__(self):
        return f'option {self.option}'