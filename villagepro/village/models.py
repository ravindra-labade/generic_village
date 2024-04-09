from django.db import models


class Village(models.Model):
    village_name = models.CharField(max_length=20)
    delivery_address = models.CharField(max_length=20)
    total_distance = models.IntegerField()
    total_population = models.IntegerField()
    village_head = models.CharField(max_length=20)


