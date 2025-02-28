from django.db import models

# Create your models here.


class Companies(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=100)
    location = models.CharField(max_length=40)
    category = models.CharField(max_length=100,choices=(
        ("IT","IT"),
        ("Non IT","Non IT"),
        ("Mobile Phones","Mobile Phones")
        ))

    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)



    def __str__(self):
        return self.name


class Employees(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    company = models.ForeignKey(Companies,on_delete=models.CASCADE)


