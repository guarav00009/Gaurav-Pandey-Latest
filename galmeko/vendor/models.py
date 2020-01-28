from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.

class Vendor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50,blank=False,null=False)
    STATUS_CHOICES = (
        (0, 'Pending'),
        (1, 'Active'),
        (2, 'Rejected'),
        (3, 'Deleted'),
    )
    status = models.IntegerField(
        _('status'), choices=STATUS_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendor'

    def __str__(self):
        return self.company_name
