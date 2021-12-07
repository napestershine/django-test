from rest_frameowrk import serializers
from models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ('id', 'email', 'username', 'address', 'password')
        extra_kwargs = {'password': {'write_only': True}}
