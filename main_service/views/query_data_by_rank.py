from rest_framework.views import APIView
from utils.response_handler import StandardizedResponse
from main_service.models.data_sales import DataSales
from main_service.serializers.data_sales import DataSalesSerializer
from rest_framework.permissions import IsAuthenticated


class GetDataByRank(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        query_by_rank = DataSales.objects.filter(rank=pk)
        if not query_by_rank:
            return StandardizedResponse(success=False, status_code=404,
                                        message='OOPS! There is no game with this rank')
        serializer = DataSalesSerializer(query_by_rank, many=True)
        return StandardizedResponse(success=True, status_code=200, data=serializer.data,
                                    message='The game with requested rank is found successfully')
