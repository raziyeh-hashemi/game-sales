from rest_framework.views import APIView
from utils.response_handler import StandardizedResponse
from main_service.models.data_sales import DataSales
from main_service.serializers.data_sales import DataSalesSerializer

class GetDataByRank(APIView):
