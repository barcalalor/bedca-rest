from rest_framework import serializers

from authentification.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class UserSerializerList(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'created']


class UserSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'created']


class UserSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class UserSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']



