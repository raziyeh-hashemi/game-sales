from rest_framework.views import APIView
from utils.response_handler import StandardizedResponse
from main_service.models.data_sales import DataSales
from main_service.serializers.data_sales import DataSalesSerializer
from rest_framework.permissions import IsAuthenticated


class GetBestData(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, platform, year):
        query_all_best = DataSales.objects.order_by('global_sales')
        query_all_best = DataSales.objects.filter(year=year).filter(platform=platform)
        query_best = []
        num = 0
        for q in query_all_best:
            if num < 5:
                query_best.append(q)
                num = num + 1
            else:
                break
        if not query_best:
            return StandardizedResponse(success=False, status_code=404,
                                        message='OOPS! There is no game with this platform in this year')
        serializer = DataSalesSerializer(query_best, many=True)
        return StandardizedResponse(success=True, status_code=200, data=serializer.data,
                                    message='The games with requested year and platform are found successfully')
