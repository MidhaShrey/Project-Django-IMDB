from watchlist_app.models import Movie
from rest_framework import serializers

# Custom Validator
def nameLength(value):
    if len(value)<2:
        raise serializers.ValidationError('InLine Validation: Name must be at least 2 characters long')

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) # It is added to make the id field read-only, so it cannot be modified by the user
    name = serializers.CharField(validators=[nameLength])
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
    
    # Field Level Validation
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Field Level: Name must be at least 2 characters long')
    #     return value
    
# Object Level Validation
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError('Object Level: Name and description cannot be the same')
    #     return data