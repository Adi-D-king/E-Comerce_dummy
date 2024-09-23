from django.db import models

# Create your models here.
class Accounts(models.Model):
    accounts_id = models.IntegerField()
    user_name = models.CharField(max_length=20)
    e_mail = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=20)

    def __str__(self):
        return self.accounts_id

