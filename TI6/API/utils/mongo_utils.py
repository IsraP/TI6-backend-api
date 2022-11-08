from rest_framework import serializers
from bson.objectid import ObjectId, InvalidId
from django.utils.encoding import smart_str

class ObjectIdField(serializers.Field):
    def to_internal_value(self, data):
        try:
            return ObjectId(str(data))
        except InvalidId:
            raise serializers.ValidationError(
                '`{}` is not a valid ObjectID'.format(data)
            )

    def to_representation(self, value):
        if not ObjectId.is_valid(value):
            raise InvalidId
        return smart_str(value)

class ObjectIdMapper():
    def to_internal_value(data):
        try:
            return ObjectId(str(data))
        except InvalidId:
            raise Exception(
                '`{}` is not a valid ObjectID'.format(data)
            )

    def to_representation(value):
        if not ObjectId.is_valid(value):
            raise InvalidId
        return smart_str(value)