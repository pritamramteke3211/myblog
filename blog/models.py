from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField
from django.utils.timezone import now

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default='')
    views= models.IntegerField(default=0)
    views_by = models.CharField(max_length=500,default='',blank=True)
    description = models.TextField(blank=True,default='')
    pub_date = models.DateField(default=now)
    thumbnail = models.ImageField(upload_to='images/blog_images', default="",null=True)
    upload_by = models.CharField(max_length=200,default='',blank=True)

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField(blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    blog = models.ForeignKey(Blogpost,on_delete=models.CASCADE,null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True) ## parent is field of self.model 
  
    reply = models.BooleanField(default=False,null=True)

    timestamp = models.DateTimeField(default=now) ## don't need add time when comment submitted

    def __str__(self):
        return str(self.sno)

