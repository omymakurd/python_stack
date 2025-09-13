from django.db import models
import re
from datetime import date
class courseManager(models.Manager):
    def course_validator(self, postData):
        errors = {}
        
        if not postData['course_name']:
            errors["missing_course_name"] = "Please Enter a course name"
        elif len(postData['course_name']) < 5:
            errors['course_name_length'] = "course name should be at least 5 characters"

       
        if not postData['desc']:
            errors["missing_ldesc"] = "Please Enter a description"
        elif len(postData['desc']) < 15:
            errors['desc_length'] = "description should be at least 15 characters"

        return errors

class Courses(models.Model):
    course_name=models.CharField(max_length=255)
    desc=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=courseManager()



