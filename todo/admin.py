from django.contrib import admin
from .models import TodoModel

class TodoModelAdmin(admin.ModelAdmin):
    model = TodoModel
    list_display = ['text','deadline','user','is_done']

admin.site.register(TodoModel,TodoModelAdmin)
