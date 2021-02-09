from django.db import models

# Create your models here.
class patient(models.Model):

    patientid = models.IntegerField()
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_no = models.IntegerField
    date_created = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    def _str_(self):
         return self.patientid


class Input(models.Model): 

 Pregnancies = models.IntegerField()
 Gulcose = models.IntegerField()
 BloodPressure = models.IntegerField()
 SkinThickness = models.IntegerField()
 Insulin = models.IntegerField()
 BMI = models.IntegerField()
 DiabetesPedigreeFunction = models.IntegerField()
 Age = models.IntegerField()
 Outcome = models.CharField(max_length=50)