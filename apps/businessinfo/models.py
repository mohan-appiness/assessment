from django.db import models

# Create your models here.

class BusinessInfo(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    logo_image = models.CharField(max_length=100, blank=True, null=True)
    about_us = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    employee_size = models.IntegerField(blank=True, null=True)
    website_link = models.URLField(max_length=250, blank=True, null=True)
    founder_name = models.CharField(max_length=100, blank=True, null=True)
    founded_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} - {self.name}'
    
    class Meta:
        db_table = 'business_informations'
        verbose_name_plural = "Business Information"
        app_label = 'businessinfo'