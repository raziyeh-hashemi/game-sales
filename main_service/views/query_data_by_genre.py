from rest_framework.views import APIView
from utils.response_handler import StandardizedResponse
from main_service.models.data_sales import DataSales
from main_service.serializers.data_sales import DataSalesSerializer
from rest_framework.permissions import IsAuthenticated


class GetDataByGenre(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, genre, pk):
        query_by_all_genre = DataSales.objects.filter(genre=genre)
        query_by_genre = []
        num = 0
        for q in query_by_all_genre:
            if num < pk:
                query_by_genre.append(q)
                num = num + 1
            else:
                break
        if not query_by_genre:
            return StandardizedResponse(success=False, status_code=404,
                                        message='OOPS! There is no game with this genre')
        serializer = DataSalesSerializer(query_by_genre, many=True)
        return StandardizedResponse(success=True, status_code=200, data=serializer.data,
                                    message='The games with requested genre are found successfully')
