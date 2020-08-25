from django.db import models
from django.contrib.auth.models import User


class Form(models.Model):
    title = models.CharField(max_length=30,default='Untitled Form')
    description = models.TextField(max_length=250,default='Description Section')
    publishDate = models.DateTimeField()
    endValidity = models.DateTimeField()
    slug = models.SlugField(max_length=50,unique_for_date='publishDate')
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'Identity - {self.slug} & Title - {self.title}'


class Section(models.Model):
    sec_title = models.CharField(max_length=30, default='Untitled Section')
    description = models.TextField(max_length=250, default='Description Section')
    form = models.ForeignKey(Form,on_delete=models.CASCADE)

    def __str__(self):
        return f'Title - {self.sec_title}'


class Field(models.Model):
    CHOICE = (
        ('text', 'TextField'),
        ('choice', 'Choices'),
        ('multipleChoices', 'MultipleChoice'),
        ('date&time', 'DateTime'),
        ('dropDown', 'DropDown'),
        ('fileUpload', 'FileUpload'),
        ('number', 'NumberOnly')
    )
    description = models.CharField(max_length=50,default='Fill This')
    label = models.CharField(max_length=50,default='Label')
    required = models.BooleanField(default=False)
    field = models.TextField(choices=CHOICE)

    def __str__(self):
        return f'Field Description - {self.description}'


