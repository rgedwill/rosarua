from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username
    
class Interpreter(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_successful_requests = models.IntegerField()
    
    def __str__(self):
        return f'interpreter: {self.user}'