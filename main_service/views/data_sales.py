from rest_framework.views import APIView
from utils.response_handler import StandardizedResponse
from main_service.models.data_sales import DataSales
from main_service.serializers.data_sales import DataSalesSerializer
from rest_framework.permissions import IsAuthenticated


class AllDataSales(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        dataSales = DataSales.objects.all()
        serializer = DataSalesSerializer(dataSales, many=True)
        return StandardizedResponse(success=True, data=serializer.data, status_code=200,
                                    message='The list of departments is shown successfully')
