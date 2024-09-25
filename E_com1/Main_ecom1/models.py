from django.db import models

# Create your models here.
class Accounts(models.Model):
    user_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    firstname = models.CharField(max_length=20,default="user_first_name")
    lastname = models.CharField(max_length=20,default="user_last_name")
    e_mail = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=20)

    def __int__(self):
        return self.user_id