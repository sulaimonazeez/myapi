from rest_framework import serializers
from .models import musicDatabased
class myData(serializers.ModelSerializer):
  class Meta:
    model = musicDatabased
    fields = '__all__'