from django.contrib import admin
from .models import Lead, Followup
# Register your models here.
admin.site.register(Followup)
admin.site.register(Lead)