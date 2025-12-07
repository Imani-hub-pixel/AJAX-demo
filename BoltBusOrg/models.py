from django.db import models

# Create your models here.
class ItemForSale(models.Model):
    name=models.CharField()
    price=models.BigIntegerField()

class Purchase(models.Model):
    purchaser=models.CharFields(max_length=200)
    item=models.ForeignKey(ItemForSale,on_delete=models.CASCADE)
    email=models.EmailField()
    price=models.ForeignKey(ItemForSale,on_delete=models.CASACDE)
    date_purchased=models.DateTimeField()
