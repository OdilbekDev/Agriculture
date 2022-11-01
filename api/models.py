from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    telegram_id = models.IntegerField()
    avatar = models.ImageField(upload_to="user/avatar")
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    balance = models.IntegerField(default=0)
    type = models.IntegerField(
        choices = (
            (1, 'Admin'),
            (2, 'Manager'),
            (3, 'Deliver'),
            (4, 'Operator'),
            (5, 'Customer'),
        ), default=5
    )


class Slider(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to='slider/img')


class Company(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="company/logo")
    description = models.TextField(null=True, blank=True)
    balance = models.IntegerField()
    workers = models.ManyToManyField(User)
    product = models.ManyToManyField('Product')
    phone_number = models.CharField(max_length=255)
    clients = models.IntegerField(default=0)
    vacancy_status = models.BooleanField(default=False)

class Category(models.Model):
    name = models.CharField(max_length=255)



    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField(default=0)
    img1 = models.ImageField(upload_to="products/img")
    img2 = models.ImageField(upload_to="products/img", blank=True, null=True)
    img3 = models.ImageField(upload_to="products/img", blank=True, null=True)
    img4 = models.ImageField(upload_to="products/img", blank=True, null=True)
    sale = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Blog(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    img = models.ImageField(upload_to='blog/images')
    img2 = models.ImageField(upload_to='blog/images', null=True, blank=True)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)



class Subject(models.Model):
    type = models.CharField(max_length=255)



class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    message = models.TextField()
    phone = models.CharField(max_length=255)



class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    text = models.TextField()
    phone = models.CharField(max_length=255)
    img = models.ImageField(upload_to='Complaint/images')
    video = models.FileField(upload_to='Complaint/Videos')

    def __str__(self) :
        return self.product.name



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total = models.IntegerField()


class Delivery_method(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CartDetail(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    subtotal = models.IntegerField()
    deliver_method = models.ForeignKey(Delivery_method, on_delete=models.CASCADE)



class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    delivery_options = models.ForeignKey(Delivery_method, on_delete=models.CASCADE)
    deliver_address = models.CharField(max_length=255)
    shipping = models.BooleanField(default=False)


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)


class Info(models.Model):
    logo = models.ImageField(upload_to="logo/")
    tg = models.URLField()
    insta = models.URLField()
    gmail = models.EmailField()
    fb = models.URLField()
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    tg_bot = models.URLField()



class Vacancy(models.Model):
    job = models.CharField(max_length=255)
    requirements = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


    def __str__(self):
        return self.job



class Card(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    cardholder_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()


    def __str__(self):
        return self.cardholder_name


class About(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()


    def __str__(self):
        return self.title


class Permissions(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Privacy_Policy(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    permissions = models.ManyToManyField(Permissions)