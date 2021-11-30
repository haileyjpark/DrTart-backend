from django.db import models
from django.db.models.expressions import OrderBy
from django.db.models.deletion    import CASCADE

from users.models    import User
from products.models import Product

class Cart(models.Model):    
    quantity   = models.IntegerField(default=0)
    price      = models.IntegerField()

    class Meta:
        db_table = 'carts'

class Order(models.Model):
    quantity     = models.IntegerField(default=0)
    created_at   = models.DateTimeField(auto_now_add=True)
    address      = models.CharField(max_length=100)
    product      = models.ForeignKey(Product, on_delete=models.CASCADE)
    user         = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'

class Orderstatus(models.Model):
    status = models.CharField(max_length=20)
    order  = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        db_table = 'orderstatus'

class Orderlist(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)

    class Meta:
        db_table = 'orderlists'