import json

from django.contrib.auth.models import User
from rest_framework import serializers
from forum.models import Message, Forum, UserProfile


class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'title', 'body', 'forum', 'creator']

    def create(self, validated_data):
        """
        Create and return a new `Forum` instance, given the validated data.
        """
        return Message.objects.create(**validated_data)


class MessageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'title', 'body', 'creator', 'created']


class CreateForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = ['id', 'title', 'description', 'creator']

    def create(self, validated_data):
        """
        Create and return a new `Forum` instance, given the validated data.
        """
        return Forum.objects.create(**validated_data)


class DetailForumSerializer(serializers.ModelSerializer):
    messages = MessageDetailSerializer(many=True)

    class Meta:
        model = Forum
        fields = ['id', 'title', 'description', 'creator', 'messages']


class ForumAddUserSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    """
    Serializer for the `Forum` model. Adds a new `User`.
    """

    def update(self, instance, validated_data):
        user = User.objects.get(id=validated_data['user'])
        instance.users.add(user)
        instance.save()
        return instance


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'title', 'description', 'creator', 'messages']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Message.objects.create(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'avatar']
