from django.db import models
import re
class userManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$')

        
        if not postData['first_name']:
            errors["missing_first_name"] = "Please Enter a First name"
        elif len(postData['first_name']) < 2:
            errors['first_name_length'] = "First name should be at least 2 characters"

        
        if not postData['last_name']:
            errors["missing_last_name"] = "Please Enter a Last name"
        elif len(postData['last_name']) < 2:
            errors['last_name_length'] = "Last name should be at least 2 characters"

        
        if not postData['email']:
            errors["missing_field_email"] = "Please Enter an email"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address"
        elif Users.objects.filter(email=postData['email']).exists():
            errors['email_exists'] = "Email already registered"

        # Password check
        password = postData.get('password')
        confirm_pw = postData.get('confirm_pw')
        if not password or not confirm_pw:
            errors["missing_field_password"] = "Please enter password and confirm it"
        elif len(password) < 8:
            errors['password_length'] = "Password should be at least 8 characters"
        elif password != confirm_pw:
            errors['password_mismatch'] = "Password and Confirm Password do not match"
        return errors 
class bookManager(models.Manager)  :      
    def book_validator(self, postData):
        errors = {}
        if not postData['title']:
             errors["missing_field_title"] = "Please Enter an book title"
        if not postData['desc']:
            errors["missing_last_desc"] = "Please Enter a Description"
        elif len(postData['desc']) < 5:
            errors['desc_length'] = "description should be at least 5 characters"

        return errors
    
class Users(models.Model):
    first_name=models.CharField( max_length=45)
    last_name=models.CharField( max_length=45)
    email=models.CharField( max_length=45)
    password=models.CharField( max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = userManager()
class books(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    uploded_by=models.ForeignKey(Users,related_name="uploded_books",on_delete=models.CASCADE)
    liked_by=models.ManyToManyField(Users,related_name="liked_books")
    objects = bookManager()

# Create your models here.
