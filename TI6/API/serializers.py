from API.models import Mamografia
from rest_framework import serializers
from API.utils.mongo_utils import ObjectIdField

class MamografiaSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)

    class Meta:
        model = Mamografia
        fields = "__all__"
