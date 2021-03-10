from django.contrib import admin

# Register your models here.
# Define a new User admin
from core.models import Camera


@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    pass

