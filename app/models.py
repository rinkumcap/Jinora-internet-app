from django.db import models

# Create your models here.
from django.db import models

class App(models.Model):
    
    PLATFORM_CHOICES = [
        ('android', 'Android'),
        ('ios', 'ios'),
    ]
    name = models.CharField(max_length=100,blank=True, null=True)  
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES) 
    tagline = models.CharField(max_length=200, blank=True, null=True) 
    logo_image= models.ImageField(upload_to="apps/",blank=True, null=True)        
    main_image = models.ImageField(upload_to="apps/",blank=True, null=True) 
    main_image1 = models.ImageField(upload_to="apps/",blank=True, null=True) 
    main_image2 = models.ImageField(upload_to="apps/",blank=True, null=True) 
    # mini_icon = models.ImageField(upload_to="apps/",blank=True, null=True) 
    download_file = models.FileField(upload_to="files/", blank=True, null=True) 
    download_link = models.URLField(blank=True, null=True) 
    download_count = models.PositiveIntegerField(default=0) 
    is_active = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)              

    def __str__(self):
        return self.name
    def __str__(self):
        return f"{self.name} ({self.platform})"
    

        # main_image2 = models.ImageField(upload_to="apps/",blank=True, null=True)   
        # mini_icon2 = models.ImageField(upload_to="apps/",blank=True, null=True) 
        # download_file2 = models.FileField(upload_to="apps/files/", blank=True, null=True) 
        # download_link2 = models.URLField(blank=True, null=True)   