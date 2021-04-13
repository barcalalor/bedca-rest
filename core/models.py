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


class ComponentType(models.Model):
    group = models.ForeignKey(ComponentGroup, on_delete=models.CASCADE, null=True)
    es_description = models.CharField(max_length=255)
    en_description = models.CharField(max_length=255)

    def __str__(self):
        return self.es_description


class Component(models.Model):
    type = models.ForeignKey(ComponentType, on_delete=models.CASCADE)
    value = models.CharField(max_length=255, null=True)
    meassure = models.CharField(max_length=255)


class Food(models.Model):
    es_description = models.CharField(max_length=255)
    en_description = models.CharField(max_length=255)
    group = models.ForeignKey(FoodGroup, on_delete=models.CASCADE)
    components = models.ManyToManyField(Component, related_name="food")

    def __str__(self):
        return self.es_description
