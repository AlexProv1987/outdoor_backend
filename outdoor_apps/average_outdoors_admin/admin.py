from django.contrib import admin
from .models import state
from outdoor_apps.average_outdoors_api.models import page, activity
# Register your models here.
admin.site.register(state)
admin.site.register(page)
admin.site.register(activity)