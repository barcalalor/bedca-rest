from django.contrib import admin

# Register your models here.
# Define a new User admin
from authentification.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
