from django.db import models
from django.contrib.auth.models import User
# from PIL import Image


class Profile(models.Model):
    """ OneToOneField will establish one to one relationship between User and Profile. on_delete will make sure
        when a User is deleted corresponding Profile is also deleted. NOT OTHER WAY AROUND. upload_to will create
        profile_pics directory in the project folder (i.e. myblogapp folder where manage.py exists"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    """ The save method get run when a Profile is saved. This method exits in the parent class. This save super class
         would first save large sized image and then override by saving a small sized image."""
    # def save(self, *args, **kwargs):
    #    super(Profile, self).save(*args, **kwargs)

    #    img = Image.open(self.image.path)

    #    if img.height > 300 or img.width > 300:
    #        output_size = (300, 300)
    #        img.thumbnail(output_size)
    #        img.save(self.image.path)
