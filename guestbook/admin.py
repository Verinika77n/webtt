# Register your models here.
from django.contrib import admin
from .models import Entry
from .models import student
from .models import group

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name', 'message')

@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'grade', 'cours')
    search_fields = ('name', 'grade', 'cours')

@admin.register(group)
class groupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cours', 'quantity')
    search_fields = ('name', 'cours')
