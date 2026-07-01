from watchlist_app.models import Review, WatchList, StreamPlatform
from rest_framework import serializers

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = '__all__'

class WatchlistSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields = '__all__'

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchlistSerializer(many=True, read_only=True) #1 # It is added to include the related watchlist objects

    # watchlist = serializers.StringRelatedField(many=True) #2 # It is added to include the related watchlist objects as string representation of the object, it will call the __str__ method of the related model and return the string representation of the object

    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True) #3 # It is added to include the related watchlist objects as primary key of the object, it will return the primary key of the related model object

    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True, 
    #     read_only=True, 
    #     view_name='watchlist-details',
    #     lookup_field='pk',
    #     lookup_url_kwarg='primary_key'
    # )
    class Meta:
        model = StreamPlatform
        fields = '__all__'


# from watchlist_app.models import Movie
# Model Serializer

# class MovieSerializer(serializers.ModelSerializer):

#     # Custom Serializer Field
#     nameLength = serializers.SerializerMethodField() # It is added to create a custom field in the serializer that is not present in the model, it is a read-only field that is calculated based on the value of another field (name in this case)

#     # defining custom field method
#     def get_nameLength(self, object):
#         return len(object.name)

#     class Meta:
#         model = Movie
#         fields = '__all__' # It is added to include all the fields of the model in the serializer, we can also specify the fields we want to include in the serializer by using a list of field names instead of '__all__'

#         # fields = ['id', 'name', 'description'] # It is added to include only the specified fields of the model in the serializer(list)

#         # Scenario: if we have 20 fields and we just want 19 fields so to implement it we can use the exclude attribute instead of fields attribute and specify the field we want to exclude from the serializer

#         # exclude = ['isActive'] # It is added to exclude the specified field from the serializer, we now not need to specify the fields we want to include in the serializer
    
#     # Field Level Validation
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError('Field Level: Name must be at least 2 characters long')
#         return value
    
    # Object Level Validation
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError('Object Level: Name and description cannot be the same')
    #     return data

# Serializer

# # Custom Validator
# def nameLength(value):
#     if len(value)<2:
#         raise serializers.ValidationError('InLine Validation: Name must be at least 2 characters long')

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True) # It is added to make the id field read-only, so it cannot be modified by the user
#     name = serializers.CharField(validators=[nameLength])
#     description = serializers.CharField()
#     isActive = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     # here instance holds old values and validated_data holds new values, so we need to update the instance with new values and save it to the database
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.isActive = validated_data.get('isActive', instance.isActive)
#         instance.save()
#         return instance
    
#     Field Level Validation
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError('Field Level: Name must be at least 2 characters long')
#         return value
    
# Object Level Validation
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Object Level: Name and description cannot be the same')
#         return data