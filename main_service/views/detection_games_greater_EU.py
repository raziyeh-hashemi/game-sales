from rest_framework.views import APIView
from utils.response_handler import StandardizedResponse
from django.db.models import F
from main_service.models.data_sales import DataSales
from main_service.serializers.data_sales import DataSalesSerializer


class GetGreaterEuroData(APIView):

    def get(self, request):
        query_greater_eu = DataSales.objects.filter(EU_sales__gt=F('NA_sales'))

        if not query_greater_eu:
            return StandardizedResponse(success=False, status_code=404,
                                        message='OOPS! There is no game with this platform in this year')
        serializer = DataSalesSerializer(query_greater_eu, many=True)
        return StandardizedResponse(success=True, status_code=200, data=serializer.data,
                                    message='The games with requested year and platform are found successfully')
