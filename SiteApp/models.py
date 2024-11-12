from django.db import models

# Create your models here.

class ProjectsModel(models.Model):
    
    SHOWSTATUS = (('YES', 'YES'), ('NO', 'NO'))
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='media/projects/', default="")
    link = models.URLField(max_length=200)
    showToSite = models.CharField(choices=SHOWSTATUS, max_length=100)
    
    def __str__(self):
        return self.title

class AchievementModel(models.Model):
    
    SHOWSTATUS = (('YES', 'YES'), ('NO', 'NO'))
    
    name = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    description = models.TextField()
    achieved = models.CharField(max_length=100)
    certificate_image = models.ImageField(upload_to='media/achievements/', default="")
    showToSite = models.CharField(choices=SHOWSTATUS, max_length=100)
    
    def __str__(self):
        return self.name
    
class ExperienceModel(models.Model):
    SHOWSTATUS = (('YES', 'YES'), ('NO', 'NO'))
    
    role = models.CharField(max_length=200)
    description = models.TextField()
    institution_name = models.CharField(max_length=200)
    certificate_image = models.ImageField(upload_to='media/experience/', default="")
    start_date = models.DateField()
    end_date = models.DateField()
    showToSite = models.CharField(choices=SHOWSTATUS, max_length=100)
    
    def __str__(self):
        return self.role + ", " + self.institution_name
    
class CertificationModel(models.Model):
    SHOWSTATUS = (('YES', 'YES'), ('NO', 'NO'))
    
    name = models.CharField(max_length=300)
    institution = models.CharField(max_length=300)
    description = models.TextField(default="")
    image = models.ImageField(upload_to='media/certification/', default="")
    
    def __str__(self):
        return self.name