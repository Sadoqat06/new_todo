from django.contrib import admin
from .models import UserModel

class UserAdmin(admin.ModelAdmin):
    model = UserModel
    list_display = ['name','surname','yosh','birth','is_student']
    search_fields = ['name','surname']

admin.site.register(UserModel,UserAdmin)
