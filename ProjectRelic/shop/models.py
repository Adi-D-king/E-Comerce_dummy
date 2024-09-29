from django.db import models

# Create your models here.
class Products(models.Model):
    product_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='PRODUCT_ID')
    title = models.TextField()
    asin = models.CharField(max_length=20)
    brand = models.CharField(max_length=100)
    stars = models.DecimalField(max_digits=2,decimal_places=1)
    reviewsCount = models.IntegerField()
    thumbnailImage = models.TextField()
    breadCrumbs = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    url = models.TextField(default='n/a')