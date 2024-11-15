from rest_framework import serializers
from api.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User 
        fields = ['id', 'username', 'first_name', 'last_name', 'date_of_birth', 'last_login_ip', 'email']

