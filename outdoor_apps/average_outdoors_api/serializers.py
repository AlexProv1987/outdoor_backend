from rest_framework import serializers
from .models import page, state, activity
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = state
        fields = ['state_name']

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = activity
        fields = ['activity_name']

class PageSerializer(serializers.ModelSerializer):
    state_reltn = StateSerializer()
    activity_reltn = ActivitySerializer()
    class Meta:
        model=page
        fields = ['state_reltn', 'activity_reltn', 'page_url']