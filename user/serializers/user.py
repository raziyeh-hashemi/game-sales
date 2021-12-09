from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'])
        return user

    class Meta:
        model = User
        fields = ('username',)
