from django.contrib import admin
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'phone_number', 'is_verified', 'created_at')
	list_filter = ('is_verified', 'created_at')
	search_fields = ('user__username', 'user__email', 'phone_number')
