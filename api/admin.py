from django.contrib import admin
from .models import Person

# Register your models here.
@admin.register(Person)
class ArticleModal(admin.ModelAdmin):
    list_filter = ('firstname', 'middlename', 'lastname')
    list_display = ('firstname', 'middlename', 'lastname')
# admin.site.register(Person)