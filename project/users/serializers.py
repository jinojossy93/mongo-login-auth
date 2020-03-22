from django.contrib.auth import authenticate, login, logout
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer

from users.models import User


class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField(label=_("Username"))
    password = serializers.CharField(label=_("Password"), style={'input_type': 'password'})

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                # From Django 1.10 onwards the `authenticate` call simply
                # returns `None` for is_active=False users.
                # (Assuming the default `ModelBackend` authentication backend.)
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg)

        attrs['user'] = user
        return attrs

class UserAddSerializer(serializers.Serializer):
    username = serializers.CharField(label=_("Username"))
    # firstname = serializers.CharField(label=_("First Name"))
    email = serializers.EmailField(label="Email")
    # lastname = serializers.CharField(label=_("Last Name"))
    password = serializers.CharField(label=_("Password"), style={'input_type': 'password'})

    def create(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        email = attrs.get('email')

        if username and password:
            user = User.create_user(username, password, email)
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg)

        attrs['username'] = user
        return attrs


class UserSerializer(DocumentSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        model = User
        fields = '__all__'
