from django.db import models


class JsonUser(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=127)
    username = models.CharField(max_length=127)
    phone = models.CharField(max_length=127)
    address_city = models.CharField(max_length=255)

    # def __str__(self):
    #    return self.name