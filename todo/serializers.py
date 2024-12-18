from rest_framework import serializers
from .models import UserModel, TodoModel

# class TodoModelSerializer(serializers.Serializer):
#     text = serializers.CharField()
#     deadline = serializers.DateTimeField()
#     is_done = serializers.BooleanField()
#     user = serializers.ModelField(UserModel)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['name','surname']


class TodoModelSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = TodoModel
        fields = ['id','text','deadline','is_done','user']

class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ['text', 'deadline','user']

class TodoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ['text', 'deadline','is_done']