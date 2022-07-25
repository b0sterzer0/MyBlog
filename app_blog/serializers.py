from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.exceptions import ValidationError
from .models import PostModel, CommentModel
from datetime import date
from app_user.serializers import UserModelSerializer


# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100, validators=[UniqueValidator(queryset=PostModel.objects)])
#     author = serializers.SlugRelatedField(slug_field='username', queryset=User.objects)
#     text = serializers.CharField()
#     add_date = serializers.DateField(format='%d.%m.%Y', read_only=True, default=date.today())
#
#     def validate(self, attrs):
#         if attrs['author'].username == 'admin':
#             raise ValidationError('Администратор не может публиковать посты')
#         return attrs
#
#     def create(self, validated_data):
#         return PostModel.objects.create(**validated_data)


class PostModelSerializer(serializers.ModelSerializer):
    author = UserModelSerializer(many=False)

    class Meta:
        model = PostModel
        fields = ['id', 'title', 'author', 'text', 'add_date']
        extra_kwargs = {
            'author': {'read_only': True}
        }


class CommentSerializer(serializers.Serializer):
    author = serializers.SlugRelatedField(slug_field='username', queryset=User.objects)
    text = serializers.CharField()
    add_comment_date = serializers.DateField(format='%d.%m.%Y', read_only=True, default=date.today())
    post = serializers.CharField(source='post.title')

    def validate(self, attrs):
        if attrs['author'].username == 'admin':
            raise ValidationError('Администратор не может оставлять комментарии')
        return attrs

    def create(self, validated_data):
        return CommentModel.objects.create(**validated_data)

