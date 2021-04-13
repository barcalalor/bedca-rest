from django.contrib import admin

# Register your models here.
# Define a new User admin
from core.models import Food, FoodGroup, ComponentGroup, Component, ComponentType


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass


@admin.register(FoodGroup)
class FoodGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(ComponentGroup)
class ComponentGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    pass

@admin.register(ComponentType)
class ComponentTypeAdmin(admin.ModelAdmin):
    search_fields=('id',)
