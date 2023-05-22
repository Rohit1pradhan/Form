from django.contrib import admin

from api.models import user


# Register your models here.
@admin.register(user)
class useradmin(admin.ModelAdmin):
    list_display = ['id','name','email','phone','dob']