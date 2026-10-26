from rest_framework import serializers
from MovieApp.models import MovieDb

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model=MovieDb
        fields="__all__"
