from django.db import models
from users.models import Accounts

# Create your models here.
class Payments(models.Model):
    payment_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    customer_id = models.ForeignKey(Accounts,on_delete=models.CASCADE)
    payment_mode = models.CharField(max_length=50)
    date_of_payment = models.DateTimeField(auto_now=True)
    payment_status = models.CharField(max_length=20)

    def __int__(self):
        return self.customer_id