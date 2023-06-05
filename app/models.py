from django.db import models
from django.contrib.auth.models import User

# Create your models here.

state_choices = [
    ("karnali", "karnali"),
    ("Gandaki", "Gandaki"),
    ("lumbini", "lumbini"),
    ("Madhesh", "Madhesh"),
    ("Bagmati", "Bagmati"),
    ("state 1", "State 1"),
]


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    state = models.CharField(choices=state_choices, max_length=20)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name


category = [
    ("mobile", "mobile"),
    ("laptop", "laptop"),
    ("car", "car"),
    ("others", "others"),
]


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    actual_price = models.IntegerField(null=True, blank=True)
    discounted_price = models.IntegerField()
    image = models.ImageField(upload_to="images/")
    category = models.CharField(max_length=20, choices=category)
    brand = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user} - {self.product} - {self.quantity}"


status_choices = [
    ("pending", "pending"),
    ("processing", "processing"),
    ("on the way", "on the way"),
    ("delivered", "delivered"),
    ("canceled", "canceled"),
]


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=status_choices, default="pending")
