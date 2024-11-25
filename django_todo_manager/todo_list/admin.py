from django.contrib import admin
from todo_list.models import ToDoItem
# Register your models here.
@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = "title", 'done', 'id'
    list_display_links = 'id', 'title'