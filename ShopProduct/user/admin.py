from django.contrib.auth.models import User
from django.contrib import admin



@admin.register(User)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email')  # Укажите, какие поля отображать в списке
    search_fields = ('username',)