from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import User, Essay, Edge

admin.site.register(User)
admin.site.register(Essay)
admin.site.register(Edge)
