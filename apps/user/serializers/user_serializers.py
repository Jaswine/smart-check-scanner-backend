from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class UserEmailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)

class UserSignInSerializer(UserEmailSerializer):
    class Meta(UserEmailSerializer.Meta):
        fields = UserEmailSerializer.Meta.fields + ('password',)

class UserSignUpSerializer(UserSignInSerializer):
    class Meta(UserSignInSerializer.Meta):
        fields = UserSignInSerializer.Meta.fields + ('username', )