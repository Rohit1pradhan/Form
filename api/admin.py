from django.contrib import admin
from api.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin




# Register your models here.
class userModelAdmin(BaseUserAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base userModelAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'email', 'name', 'dob','phone', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('user credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name','dob','phone',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'dob','phone', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email', 'id')
    filter_horizontal = ()


# Now register the new userModelAdmin...
admin.site.register(User, userModelAdmin)