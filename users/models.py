import profile
from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Citizen(models.Model):
    """Model definition for Citizen."""
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture=models.ImageField(upload_to="citizen_pictures/")
    phone=models.CharField(max_length=255)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Citizen."""

        verbose_name = 'Citizen'
        verbose_name_plural = 'Citizens'

    def __str__(self):
        """Unicode representation of Citizen."""
        return f'{self.user.first_name} {self.user.last_name}'

  

class Agency(models.Model):
    """Model definition for Agency."""
    name=models.CharField(max_length=255)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Agency."""

        verbose_name = 'Agency'
        verbose_name_plural = 'Agencies'

    def __str__(self):
        """Unicode representation of Agency."""
        return f'{self.name}'

        

   

    # TODO: Define custom methods here




class Officer(models.Model):
    """Model definition for Officer."""
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    location=models.CharField(max_length=255)
    profile_picture=models.ImageField(upload_to="officer_pictures/")
    agency=models.ForeignKey(Agency, on_delete=models.CASCADE)

    

    # TODO: Define fields here

    class Meta:
        """Meta definition for Officer."""

        verbose_name = 'Officer'
        verbose_name_plural = 'Officers'

    def __str__(self):
        """Unicode representation of Officer."""
        return f'{self.user.first_name} {self.user.last_name}'

        

    # TODO: Define custom methods here




class Message(models.Model):
    """Model definition for Message."""
    citizen=models.ForeignKey(Citizen,on_delete=models.CASCADE)
    officer=models.ForeignKey(Officer,on_delete=models.CASCADE)
    


    # TODO: Define fields here

    class Meta:
        """Meta definition for Message."""

        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        """Unicode representation of Message."""
        pass

    def save(self):
        """Save method for Message."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Message."""
        return ('')

    # TODO: Define custom methods here
