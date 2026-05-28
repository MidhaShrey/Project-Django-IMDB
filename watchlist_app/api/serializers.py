from watchlist_app.models import Movie
from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) # It is added to make the id field read-only, so it cannot be modified by the user
    name = serializers.CharField()
    description = serializers.CharField()
    isActive = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    # here instance holds old values and validated_data holds new values, so we need to update the instance with new values and save it to the database
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.isActive = validated_data.get('isActive', instance.isActive)
        instance.save()
        return instance