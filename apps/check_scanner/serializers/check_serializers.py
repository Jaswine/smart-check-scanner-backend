from rest_framework.serializers import ModelSerializer

from apps.check_scanner.models import Check


class BaseCheckSerializer(ModelSerializer):
    """
        Base serializer for Check model.
    """
    class Meta:
        model = Check
        fields = ('file', )

class CheckSerializer(BaseCheckSerializer):
    """
        Serializer for Check model.
    """
    class Meta(BaseCheckSerializer.Meta):
        fields = BaseCheckSerializer.Meta.fields + ('recommendations', 'status', 'created_at',)

class CreateCheckSerializer(BaseCheckSerializer):
    """
        Serializer for creating a new Check model.
    """
    class Meta(BaseCheckSerializer.Meta):
        fields = BaseCheckSerializer.Meta.fields