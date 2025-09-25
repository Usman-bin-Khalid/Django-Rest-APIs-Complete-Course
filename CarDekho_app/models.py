from django.db import models
from django.core.exceptions import ValidationError


def alphanumeric(value):
    if not str(value).isalnum():
        raise ValidationError("Only alphabets and numbers are allowed")


class ShowRoomList(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=200)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

# Create your models here.
class CarList(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=200)
  active = models.BooleanField(default=False)
  chassisnumber = models.CharField(max_length=100, null=True, blank=True, validators =[alphanumeric])
  price = models.DecimalField(max_digits=9 , decimal_places=2, blank=True, null=True)

  def __str__(self):
      return self.name




def __str__(self):
    return self.name

