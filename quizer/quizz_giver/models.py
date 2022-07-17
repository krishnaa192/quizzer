from curses import def_prog_mode
from email.headerregistry import Address
from email.policy import default
from django.db import models
from pkg_resources import require
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
import uuid
# Create your models her
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    username=models.CharField(max_length=10)
    Name=models.CharField(max_length=200,blank=True,null=True)
    email=models.EmailField(max_length=200, null=True)
    Bio=models.TextField(blank=True,null=True)
    tel=models.CharField(max_length=20, default="")
    work=models.TextField(default="")
    designation=models.CharField(max_length=200,default='None')
    gender=(
        ('male','male'),
       ('female','female'),
        ('other','others')
    )
    gender=models.CharField(max_length=22,choices=gender,default="")
    Address=models.TextField(default='None')
    def __str__(self):
        return self.Name


class Quizes(models.Model):
    diff_choices=(
        ('easy', 'easy'),
        ('medium', 'medium'),
        ('hard','hard'),
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    quiz_name=models.CharField(max_length=100,null=True , blank=True)
    time=models.IntegerField(help_text="Duration of quiz in minutes",null=True , blank=True)
    topic=models.CharField(max_length=200,null=True , blank=True)
    require_score=models.IntegerField(help_text=" require score in %",null=True , blank=True)
    

    def __str__(self):
        return self.quiz_name

    
    
class QuesModel(models.Model):
    quiz_name=models.ForeignKey(Quizes,on_delete=models.CASCADE,name="quiz_name")
    question = RichTextField(default="None")
    option1 =RichTextField()
    option2 = RichTextField()
    option3 = RichTextField()
    option4 = RichTextField()
    op=(
        ('option1', 'option1'),
        ('option2', 'option2'),
        ('option3','option3'),
        ('option4','option4'),
    )
    ans = RichTextField(max_length=12, choices=op)
    
    def __str__(self):
        return self.question

class Results(models.Model):
    get_score=models.IntegerField()
    percent=models.CharField(max_length=200)
    names_quizer=models.CharField(max_length=200)




    





