from rest_framework.response import Response
from rest_framework import serializers


def get_response_serializer(data_serializer: serializers.Serializer):
    class ResponseDataSerializer(serializers.Serializer):
        message = serializers.CharField
        success = serializers.BooleanField
        data = data_serializer

    return ResponseDataSerializer


class StandardizedResponse(Response):

    def __init__(self, success: bool, status_code: int, data=None, message=None):
        self.status_code = status_code
        self.success = success
        super_data = {
            'data': data,
            'message': message,
            'success': success,
        }
        self.message = message
        super().__init__(super_data, status=status_code)
