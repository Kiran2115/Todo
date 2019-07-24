from rest_framework import serializers
from .models import *
from users.serializers import UserSerializer


class TodoSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    # user = UserSerializer()
    class Meta:
        model = TodoList
        fields = '__all__'
        extra_kwargs = {
            'url': {
                'view_name': 'todolist:todo-detail'
            }
        }
        
        """def create(self, validated_data):
            id_obj= TodoList(**validated_data)
            id_obj.save()
            return id_obj

        def update(self, instance, validated_data):
            instance.name = validated_data["id_no"]
            instance.save()
            return instance"""