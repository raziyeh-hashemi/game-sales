from rest_framework.views import APIView
from utils.response_handler import StandardizedResponse
from main_service.models.data_sales import DataSales
from main_service.serializers.data_sales import DataSalesSerializer
from rest_framework.permissions import IsAuthenticated


class SearchByName(APIView):
    permission_classes = (IsAuthenticated,)
    ordering_fields = '__all__'

    def get(self, request, name):
        query_contain_name = DataSales.objects.filter(name__contains=name)

        if not query_contain_name:
            return StandardizedResponse(success=False, status_code=404,
                                        message='OOPS! There is no game with this name')
        serializer = DataSalesSerializer(query_contain_name, many=True)
        return StandardizedResponse(success=True, status_code=200, data=serializer.data,
                                    message='The games with requested name are found successfully')
