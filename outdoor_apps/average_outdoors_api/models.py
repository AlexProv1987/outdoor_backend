from django.db import models
from outdoor_apps.average_outdoors_admin.models import state
# Create your models here.
class activity(models.Model):
    activity_name = models.CharField(max_length=100)

    def __str__(self):
        return self.activity_name
    
class page(models.Model):
    state_reltn = models.ForeignKey(state,on_delete=models.CASCADE)
    page_url = models.URLField()
    activity_reltn = models.ForeignKey(activity, on_delete=models.PROTECT)