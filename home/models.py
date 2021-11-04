from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Brach(models.Model):
    brach = models.CharField(max_length=50)
    created_Date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.brach
    
class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_teacher =models.EmailField(max_length=254)
    phone_teacher = models.CharField(max_length=50)
    image = models.ImageField(upload_to="teacher", default="default.png")
    speciality = models.ForeignKey(Brach, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.first_name + " "+ self.last_name