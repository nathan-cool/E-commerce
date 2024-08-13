from django.db import models
import datetime

# Category model represents a product category
class Category(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = 'categories'

# Customer model represents a customer in the e-commerce store
class Customer(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  phone = models.CharField(max_length=255)
  password = models.CharField(max_length=500)

  def __str__(self):
    return self.name
  
# Product model represents a product in the e-commerce store
class Product(models.Model):
  name = models.CharField(max_length=255)
  price = models.FloatField(default=0)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
  description = models.CharField(max_length=255, default='', null=True, blank=True)
  image = models.ImageField(upload_to='uploads/products/')
  is_sale = models.BooleanField(default=False)
  sale_price = models.FloatField(default=0)

  def __str__(self):
    return self.name

# Order model represents an order placed by a customer
class Order(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  quantity = models.IntegerField(default=1)
  price = models.FloatField()
  address = models.CharField(max_length=255)
  phone = models.CharField(max_length=255, default='', null=True, blank=True)
  date = models.DateField(default=datetime.datetime.today)
  status = models.BooleanField(default=False)

  def __str__(self):
    return self.product.name