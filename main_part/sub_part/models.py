from django.db import models

# Create your models here.
class customer_register_table(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email_id=models.EmailField(max_length=50)
    phone_number=models.CharField(max_length=15)
    password=models.CharField(max_length=50)
    otp_number=models.CharField(max_length=20)

    #def __str__(self):
    #    return self.first_name
