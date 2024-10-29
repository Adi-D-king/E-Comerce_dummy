from django.db import models
from orders.models import Orders
from users.models import Accounts

# Create your models here.
class Payments(models.Model):
    payment_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    order_id = models.ForeignKey(Orders,on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Accounts,on_delete=models.CASCADE)
    Payment_mode = models.CharField(max_length=50)
    date_of_payment = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.customer_id
    

class PaymentsDetails(models.Model):
    payment_id = models.ForeignKey(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    paymentmode = models.CharField(max_length=50)