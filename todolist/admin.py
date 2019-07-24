from django.contrib import admin

from . import models 


class TodoListAdmin(admin.ModelAdmin):
    list_display = ("id_no","title",  "created_date", "discription")


admin.site.register(models.TodoList, TodoListAdmin)
