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
