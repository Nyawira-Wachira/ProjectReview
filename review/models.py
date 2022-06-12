from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='Default.png', upload_to='profile_pics')
    bio = models.TextField()
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} Profile'

