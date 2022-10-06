from rest_framework import serializers
from bson.objectid import ObjectId, InvalidId
from django.utils.encoding import smart_str

class ObjectIdField(serializers.Field):
    """ Serializer field for Djongo ObjectID fields """
    def to_internal_value(self, data):
        # Serialized value -> Database value
        try:
            return ObjectId(str(data))  # Get the ID, then build an ObjectID instance using it
        except InvalidId:
            raise serializers.ValidationError(
                '`{}` is not a valid ObjectID'.format(data)
            )

    def to_representation(self, value):
        # Database value -> Serialized value
        if not ObjectId.is_valid(value):  # User submitted ID's might not be properly structured
            raise InvalidId
        return smart_str(value)

class ObjectIdMapper():
    def to_internal_value(data):
        # Serialized value -> Database value
        try:
            return ObjectId(str(data))  # Get the ID, then build an ObjectID instance using it
        except InvalidId:
            raise Exception(
                '`{}` is not a valid ObjectID'.format(data)
            )

    def to_representation(value):
        # Database value -> Serialized value
        if not ObjectId.is_valid(value):  # User submitted ID's might not be properly structured
            raise InvalidId
        return smart_str(value)