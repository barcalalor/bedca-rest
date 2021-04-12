from django.db import models


# Masters


class FoodGroup(models.Model):
    es_description = models.CharField(max_length=255)
    en_description = models.CharField(max_length=255)

    def __str__(self):
        return self.es_description


class ComponentGroup(models.Model):
    es_description = models.CharField(max_length=255)
    en_description = models.CharField(max_length=255)

    def __str__(self):
        return self.es_description


class Component(models.Model):
    es_description = models.CharField(max_length=255)
    en_description = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    meassure = models.CharField(max_length=255)
    group = models.ForeignKey(ComponentGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.es_description


class Food(models.Model):
    es_description = models.CharField(max_length=255)
    en_description = models.CharField(max_length=255)
    group = models.ForeignKey(FoodGroup, on_delete=models.CASCADE)
    components = models.ManyToManyField(Component, related_name="food")

    def __str__(self):
        return self.es_description
