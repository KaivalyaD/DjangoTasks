from django.contrib import admin
from .models import User as extended_user

admin.site.register(extended_user)
