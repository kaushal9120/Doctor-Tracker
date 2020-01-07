from django.db import models

# Create your models here.
class User(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    otp=models.IntegerField(default=459)
    is_active=models.BooleanField(default=True)
    is_verfied=models.BooleanField(default=False)
    role=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True,blank=False)
    updated_at=models.DateTimeField(auto_now=True,blank=False)
    

class Doctor(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    qualification=models.CharField(max_length=100)
    speciality=models.CharField(max_length=100)
    mobile=models.CharField(max_length=10)
    clinic=models.CharField(max_length=100,blank=True)
    address=models.CharField(max_length=500,blank=True)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50,blank=True)
    gender=models.CharField(max_length=10)
    birthdate=models.DateField()
    profile_pic=models.ImageField(upload_to="img/",default="abc.jpg")

class Patient(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=500,blank=True)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50,blank=True)
    gender=models.CharField(max_length=10)
    birthdate=models.DateField()
    #pic2=models.ImageField(upload_to="img/",default="can.jpg")
