from django.db import models
import re
from datetime import date
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

      
        password = postData.get('password')
        confirm_pw = postData.get('confirm_pw')
        if not password or not confirm_pw:
            errors["missing_field_password"] = "Please enter password and confirm it"
        elif len(password) < 8:
            errors['password_length'] = "Password should be at least 8 characters"
        elif password != confirm_pw:
            errors['password_mismatch'] = "Password and Confirm Password do not match"

      
        if postData.get('birthday'):
            birthday_str = postData['birthday']
            if len(birthday_str.split("-")) == 3:
                year, month, day = birthday_str.split("-")
                if year.isdigit() and month.isdigit() and day.isdigit():
                    birthday = date(int(year), int(month), int(day))
                    today = date.today()

                    if birthday >= today:
                        errors['birthday_future'] = "Birthday must be in the past"
                    else:
                        age = today.year - birthday.year - (
                            (today.month, today.day) < (birthday.month, birthday.day)
                        )
                        if age < 13:
                            errors['birthday_age'] = "You must be at least 13 years old to register"
                else:
                    errors['birthday_invalid'] = "Invalid birthday format (must be YYYY-MM-DD)"
            else:
                errors['birthday_invalid'] = "Invalid birthday format (must be YYYY-MM-DD)"
        

        return errors
class messageManger(models.Manager):
    def message_validator(self, postData):
        errors = {}
        if not postData['message']:
            errors["missing_message"] = "Please Enter a message"
        elif len(postData['message']) < 2:
            errors['messagee_length'] = "First name should be at least 2 characters"
        return errors  
class commentManger(models.Manager):
    def comment_validator(self, postData):
        errors = {}
        if not postData['comment']:
            errors["missing_comment"] = "Please Enter a comment"
        elif len(postData['comment']) < 2:
            errors['comment_length'] = "comment should be at least 2 characters"
        return errors 
class Users(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password =models.CharField(max_length=255)
    birthday = models.DateField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=userManager()
class Messages(models.Model):
    user=models.ForeignKey(Users,related_name="messages",on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=messageManger()
class Comments(models.Model):
    message=models.ForeignKey(Messages,related_name="comments",on_delete=models.CASCADE)
    user=models.ForeignKey(Users,related_name="comments",on_delete=models.CASCADE)
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=commentManger()


