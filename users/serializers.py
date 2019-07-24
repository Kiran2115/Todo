from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

        password = serializers.CharField(write_only=True)
        set_password = serializers.CharField(write_only=True)
        #username = serializers.CharField(write_only=True)




        def create(self, validated_data):
            user = User(
                username=validated_data.get('username', None)
            )

            user.set_password(validated_data.get('password', None))
            user.email = validated_data.get('email', None)
            # user.set_password(user.password)
            user.save()
            return user

        def update(self, instance, validated_data):
            for field in validated_data:
                if field == 'password':
                    instance.set_password(validated_data.get(field))
                else:
                    instance.__setattr__(field, validated_data.get(field))
            instance.save()
            return instance

        class Meta:
            model = User
            fields = ['username', 'email','password','set_password']
            # fields = '__all__'
            extra_kwargs = {
                'url': {
                    'view_name': 'users:user-detail',
                }
            }