from django.db import models

class Trait(models.Model):
    name = models.CharField(max_length=256)
    
class InterpretationRequest(models.Model):
    datetime_created = models.DateTimeField(auto_now_add=True)
    traits = models.ManyToManyField(Trait)
    
