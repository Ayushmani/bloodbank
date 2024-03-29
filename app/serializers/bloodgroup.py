# import libraries
from rest_framework import serializers

# import models
from app.models import BloodGroup

class BloodGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = BloodGroup
        fields = ('id', 'name', 'description')

    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.id = attrs.get('id', instance.id)
            instance.name = attrs.get('name', instance.name)
            instance.description = attrs.get('description', instance.description)
            return instance

        # Create new instance
        return BloodGroup(**attrs)
