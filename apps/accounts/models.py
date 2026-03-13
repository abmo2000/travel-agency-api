import uuid

from django.conf import settings
from django.db import models


class Account(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name='account',
	)
	phone_number = models.CharField(max_length=11, blank=True)
	date_of_birth = models.DateField(null=True, blank=True)
	avatar = models.ImageField(upload_to='accounts/avatars/', null=True, blank=True)
	address = models.CharField(max_length=255, blank=True)
	city = models.CharField(max_length=120, blank=True)
	country = models.CharField(max_length=120, blank=True)
	is_verified = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return f"Account<{self.user.username}>"
