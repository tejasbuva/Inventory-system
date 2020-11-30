from django.contrib.auth.models import User, Group
from django.db import models
from tagging.fields import TagField


# Create your models here.

class Product(models.Model):
    situation = (
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable'),
    )
    Product_Name = models.CharField(max_length=30, blank=True)
    Status = models.CharField(max_length=30, choices=situation)
    Serial_No = models.CharField(max_length=30, unique=True)
    Issues = models.CharField(max_length=280, blank=True)
    Cost_in_Euro = models.PositiveIntegerField(default=0, blank=True)
    # Units = models.PositiveIntegerField(default=100, blank=True)
    Description = models.TextField(max_length=280, blank=True)
    User_Name = models.ForeignKey(User, default=1, on_delete=models.CASCADE, null=True, blank=True)
    Product_Group = models.ForeignKey(Group, default=1, on_delete=models.CASCADE, null=True, blank=True)
    Purchase_Date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    Date_Modified = models.DateField(auto_now_add=True, blank=True)
    Tags = TagField()

    def __unicode__(self):
        return self.Product_Name

    def product_tags(self):
        return self.Tags.split(',')
        # return ['Tag1', 'Tag2', 'Tag3', 'Tag4', 'Tag5']

