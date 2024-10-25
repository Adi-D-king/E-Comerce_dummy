from django.db import models

# Create your models here.
class Accounts(models.Model):
    user_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    firstname = models.CharField(max_length=20,default="user_first_name")
    lastname = models.CharField(max_length=20,default="user_last_name")
    e_mail = models.EmailField(max_length=20,unique=True)
    phone_no = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20,unique=True,default='N/A')
    cart_id = models.IntegerField(default=None)  #need to be changed

    def __int__(self):
        return self.user_id
    
class Address(models.Model):
    Address_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    house_no = models.CharField(max_length=200,unique=False)
    colony = models.CharField(max_length=200,unique=False)
    village = models.CharField(max_length=200,unique=False)
    street = models.CharField(max_length=200,unique=False)
    state = models.CharField(max_length=200,unique=False)
    city = models.CharField(max_length=200,unique=False)
    pincode = models.CharField(max_length=10,unique=False)
    customer_id = models.ForeignKey(Accounts,on_delete=models.CASCADE)