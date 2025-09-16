from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from api.models import Room, User


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'email', 'password','first_name','last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            name=validated_data.get("name", ""),
            password=validated_data["password"],
            first_name=validated_data.get("first_name",""),
            last_name=validated_data.get("last_name","")
        )
        groups, _ = Group.objects.get_or_create(name='USER')
        user.groups.add(groups)
        return user


# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         # Thêm thôn tin custome vào JWT
#         token['username'] = user.username
#         token['roles'] = [g.name for g in user.groups.all()]
#         return token
#
#     def validate(self, attrs):
#         data = super().validate(attrs)
#         data["username"] = self.user.username
#         data["roles"] = [g.name for g in self.user.groups.all()]
#         return data
