from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
import uuid

from django.db.models.signals import post_save
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default.png', upload_to='profile_pics')
    bio = models.TextField()
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)   

class Project(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80) 
    image=models.ImageField(upload_to=user_directory_path, verbose_name='Picture', null=False)
    description=models.TextField(max_length=300, verbose_name='Caption')
    posted = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=500)

    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

class Review(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    design = models.IntegerField()
    usability = models.IntegerField() 
    content = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
   

  
