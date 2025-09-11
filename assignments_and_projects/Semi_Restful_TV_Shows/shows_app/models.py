from django.db import models
import datetime


class ShowManager(models.Manager):
    def show_validator(self,postData,show_id=None):
        errors={}
        if not postData['title']:
            errors["missing_field_title"]="Please Enter a Title"
        elif len(postData['title'])<2:
            errors['title_length']="Title shoud ba at least 2 characters"
        else:
            qs=Show.objects.filter(title=postData['title'])
            if show_id:
                qs=qs.exclude(id=show_id)
            if qs.exists():
                errors['title_unique']="Title must be unique"

        if not postData['network']:
            errors["missing_field_network"]="Please Enter a Network"
        else:
            if len(postData['network'])<3:
                errors['network_length']="network shoud ba at least 3 characters"

        if not postData['release_date']:
            errors["missing_field_release_date"]="Please Enter Release date"
        else:
           try:
              release_date=datetime.datetime.strptime(postData['release_date'],"%Y-%m-%d").date()  
              if release_date > datetime.date.today():
                  errors['release_date_future']="Release date must be in the past"
           except ValueError:
               errors['invalid_date']="Invalid date format (YYYY-MM-DD required)"
       
        if  postData['desc']:
            
           if len(postData['desc'])<10:
                errors['desc_length']="Description shoud ba at least 10 characters"
        return errors
class Show(models.Model):
    title=models.CharField(max_length=45)
    network=models.CharField(max_length=45)
    release_date=models.DateField()
    desc=models.TextField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=ShowManager()
# Create your models here.
