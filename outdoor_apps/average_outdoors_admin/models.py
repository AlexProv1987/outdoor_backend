from django.db import models

# Create your models here.
class state(models.Model):
    state_name = models.CharField(max_length=50, db_index=True)
    state_abbr = models.CharField(max_length=5)

    def __str__(self) -> str:
        return self.state_name

class county(models.Model):
    county_name = models.CharField(max_length=50)
    state_id = models.ForeignKey(state, on_delete=models.PROTECT)
'''
class recommended_camps(models.Model):
    camp_name = models.CharField(max_length=100)
    state_id = models.ForeignKey(state, on_delete=models.PROTECT)

class conservation_pages(models.Model):
    site_name = models.CharField(max_length=100)
    state_id = models.ForeignKey(state,on_delete=models.PROTECT)
'''