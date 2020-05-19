from rest_framework import serializers
from .models import UserInfo

class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('userId', 'password', 'email','birth', 'gender')

    #def create(self, validated_data):
    #    return UserInfo.objects.create(**validated_data)

    #def update(self, instance, validate_data):
     #   instance.userId = validate_data.get('userId', instance.userId)
     #   instance.password = validate_data.get('password', instance.password)
     #   instance.birth = validate_data.get('birth', instance.birth)
     #   instance.gender = validate_data.get('gender', instance.gender)
     #   instance.save()
     #   return instance