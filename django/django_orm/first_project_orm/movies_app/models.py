from django.db import models
class Director(models.Model):
    name=models.CharField(max_length=45)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
class Movies(models.Model):
    title=models.CharField(max_length=45)
    description=models.TextField()
    relese_data=models.DateTimeField()
    duration=models.IntegerField()
    director=models.ForeignKey(Director,related_name="movies",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


# Create your models here.
