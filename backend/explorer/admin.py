from django.contrib import admin

from .models import OperationalUnit, Oilfield, Well

admin.site.register(OperationalUnit)
admin.site.register(Oilfield)
admin.site.register(Well)