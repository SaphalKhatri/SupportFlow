from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('agent', 'Support Agent'),
        ('admin', 'Administrator'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='customer',
    )
    def is_customer(self) -> bool:
        return self.role == 'customer'
    def is_agent(self)->bool:
        return self.role=='agent'
    def is_admin(self)->bool:
        return self.role=='admin'
    def __str__(self):
        return f'{self.username}-{self.get_role-display()}'