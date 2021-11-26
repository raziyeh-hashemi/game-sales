from rest_framework.views import APIView
from utils.response_handler import StandardizedResponse
from main_service.models.data_sales import DataSales
from main_service.serializers.data_sales import DataSalesSerializer


class GetDataByYear(APIView):

    def get(self, request, year, pk):
        query_by_all_year = DataSales.objects.filter(year=year)
        query_by_year = []
        num = 0
        for q in query_by_all_year:
            if num < pk:
                query_by_year.append(q)
                num = num + 1
            else:
                break
        if not query_by_year:
            return StandardizedResponse(success=False, status_code=404,
                                        message='OOPS! There is no game with this year')
        serializer = DataSalesSerializer(query_by_year, many=True)
        return StandardizedResponse(success=True, status_code=200, data=serializer.data,
                                    message='The games with requested year are found successfully')
