from django.db import models

class Staffdb(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Date = models.CharField(max_length=50, null=True, blank=True)
    Image = models.ImageField(upload_to='profile/',null=True,blank=True)

class Ticketdb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Description = models.CharField(max_length=50, null=True, blank=True)
    Rate = models.IntegerField(null=True,blank=True)

class Activitydb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Role = models.CharField(max_length=50, null=True, blank=True)
    Description = models.CharField(max_length=50, null=True, blank=True)
    Duration = models.CharField(max_length=50, null=True, blank=True)
    Content = models.CharField(max_length=150, null=True, blank=True)
    Image = models.ImageField(upload_to='profile/',null=True,blank=True)

class Gallerydb(models.Model):
    Image = models.ImageField(upload_to='profile/', null=True, blank=True)

class Feedbackdb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Phone = models.IntegerField(null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Message = models.CharField(max_length=50, null=True, blank=True)

class FamilyTicketdb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Date = models.CharField(max_length=50, null=True, blank=True)
    Amount = models.CharField(max_length=50,null=True, blank=True)

class BirthdayTicketdb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Date = models.CharField(max_length=50, null=True, blank=True)
    Guests = models.IntegerField(null=True, blank=True)
    Age =  models.IntegerField(null=True, blank=True)

class SchoolTicketdb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Date = models.CharField(max_length=50, null=True, blank=True)
# Create your models here.
