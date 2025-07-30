from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Create your models here.

class customUser(AbstractUser):
    name= models.CharField(max_length= 200)
    username= models.CharField(max_length= 200, unique= True)
    email= models.EmailField(blank= True, null= True)
    bio= models.TextField(blank= True, null= True)
    avatar= models.ImageField(null= True, blank= True, upload_to= 'avatars/')

    USERNAME_FIELD= 'username'
    REQUIRED_FIELDS= []

    def __str__(self):
        return self.username
    

class Post(models.Model):
    user= models.ForeignKey(customUser, on_delete= models.CASCADE)
    text= models.TextField(null= True, blank= True)
    image= models.ImageField(null= True, blank= True, upload_to= 'posts/')
    likes= models.ManyToManyField(customUser, related_name= 'liked_posts', blank= True)
    updated= models.DateTimeField(auto_now= True)
    created= models.DateTimeField(auto_now_add= True)

    def clean(self):
        if not self.text and not self.image:
            raise ValidationError('Post can not be empty')

    @property
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.text[0:50]
    

class Comment(models.Model):
    user= models.ForeignKey(customUser, on_delete= models.CASCADE)
    post= models.ForeignKey(Post, on_delete= models.CASCADE)
    text= models.CharField(max_length= 200)
    updated= models.DateTimeField(auto_now= True)
    created= models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.text[0:50]