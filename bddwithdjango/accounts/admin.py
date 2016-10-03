from django.contrib import admin

# Register your models here
from .models import User, Interest


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    pass

