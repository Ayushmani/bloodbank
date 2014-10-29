# import libraries
from rest_framework import serializers

# import models
from app.models import Individual

class IndividualSerializer(serializers.ModelSerializer):

    class Meta:
        model = Individual
        fields = ('id', 'bloodgroup', 'name', 'phone_number')

    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.id = attrs.get('id', instance.id)
            instance.bloodgroup = attrs.get('bloodgroup', instance.bloodgroup)
            instance.name = attrs.get('name', instance.name)
            instance.phone_number = attrs.get('phone_number', instance.phone_number)
            return instance

        # Create new instance
        return Individual(**attrs)
