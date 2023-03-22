from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = ("Contact")
