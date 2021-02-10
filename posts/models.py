from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import truncatechars 
from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce import HTMLField

# Create your models here.


User = get_user_model()

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Author(models.Model):
    user          = models.OneToOneField(User, on_delete=models.CASCADE)
    content       = models.TextField()
    profile_image = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name      = models.CharField(max_length=20)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title    = models.CharField(max_length=80)
    slug     = models.SlugField()
    content  = models.TextField()
    overview = HTMLField()
    author   = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='categories')
    image    = models.ImageField()
    previous_post = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='previous', blank=True, null=True)
    next_post     = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='next', blank=True, null=True)
    # create_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    @property
    def short_description(self):
        return truncatechars(self.content, 20)

    def get_absolute_url(self):
        return reverse('post_details', kwargs={
            'id': self.id
        })

    @property
    def get_comments(self):
        return self.comments.all()

class Comment(models.Model):
    content   = models.TextField()
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    post      = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username