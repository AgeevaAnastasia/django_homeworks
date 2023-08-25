from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    registration = models.DateField(auto_now=True)

    def __str__(self):
        return f'Username: {self.name} {self.lastname}, email: {self.email}, phone: {self.phone}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    amount = models.IntegerField()
    add_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'Product:: {self.name}, price: {self.price}, ' \
               f'amount: {self.amount}'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateField(auto_now=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'Customer:: {self.customer}, products: {self.products}, ' \
               f'date: {self.date_ordered}, price: {self.total_price}'
