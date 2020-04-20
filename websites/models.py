from django.db import models


class Website(models.Model):
    """
    Website model
    """
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    details = models.TextField(blank=True)
    details2 = models.TextField(blank=True)
    details3 = models.TextField(blank=True)
    details4 = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
