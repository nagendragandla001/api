from rest_framework import serializers
from JobsApp.models import Jobs

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ('id', 'name', 'city', 'status', 'posted_on', 'posted_by')
