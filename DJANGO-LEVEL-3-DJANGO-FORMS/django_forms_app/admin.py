from django.contrib import admin

# Register your models here.
from .models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    pass

admin.site.register(Review, ReviewAdmin)
