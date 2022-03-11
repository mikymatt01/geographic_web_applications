from django.contrib.gis import admin
from .models import Italy

# Register your models here.
admin.site.register(Italy, admin.ModelAdmin)