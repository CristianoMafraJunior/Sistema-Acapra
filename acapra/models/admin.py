from django.db import models


class Admin(models.Model):
    login = models.CharField(max_length=100)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.login
