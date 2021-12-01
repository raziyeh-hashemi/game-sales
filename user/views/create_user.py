from rest_framework.permissions import AllowAny
from utils.response_handler import StandardizedResponse
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from user.serializers.user import UserSerializer, User


class CreateUserView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return StandardizedResponse(success=True, status_code=201, data=[serializer.data, token.key],
                                            message='user is created')
        return StandardizedResponse(success=False, status_code=400, data=serializer.errors,
                                    message='bad request')
