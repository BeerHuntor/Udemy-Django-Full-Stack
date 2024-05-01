from django.contrib import admin
from ProTwo_App.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    fields = ["first_name", "last_name", "email"]

admin.site.register(User, UserAdmin)
