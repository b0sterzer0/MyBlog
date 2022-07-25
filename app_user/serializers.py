from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from .models import ProfileModel
from django.core.validators import MaxValueValidator
from rest_framework import serializers
from datetime import date
from rest_framework.validators import UniqueTogetherValidator


class ProfileSerializer(serializers.Serializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects)
    city = serializers.CharField()
    date_of_birth = serializers.DateField(
        format='%d.%m.%Y',
        input_formats=['%d.%m.%Y', 'iso-8601'],
        validators=[MaxValueValidator(date(2022, 7, 22))]
    )
    hobby = serializers.CharField()

    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=ProfileModel.objects,
                fields=['user', 'city', 'date_of_birth']
            ),
        ]

    def validate(self, attrs):
        data_set = {attrs['user'], attrs['city'], attrs['date_of_birth']}
        if len(data_set) != 3:
            raise ValidationError('Данные не могут совпадать', code='duplicate values')
        return attrs

    def create(self, validated_data):
        return ProfileModel.objects.create(**validated_data)


class UserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['password', 'last_login']
