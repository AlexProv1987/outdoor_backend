from django.db import models

# Create your models here.
class state(models.Model):
    state_name = models.CharField(max_length=50)
    state_abbr = models.CharField(max_length=5)

    def __str__(self) -> str:
        return self.state_name
class county(models.Model):
    county_name = models.CharField(max_length=50)
    state_id = models.ForeignKey(state, on_delete=models.CASCADE)