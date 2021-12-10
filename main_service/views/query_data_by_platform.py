from rest_framework.views import APIView
from utils.response_handler import StandardizedResponse
from main_service.models.data_sales import DataSales
from main_service.serializers.data_sales import DataSalesSerializer
from rest_framework.permissions import IsAuthenticated


class GetDataByPlatform(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, platform, pk):
        query_by_all_platform = DataSales.objects.filter(platform=platform)
        query_by_platform = []
        num = 0
        for q in query_by_all_platform:
            if num < pk:
                query_by_platform.append(q)
                num = num + 1
            else:
                break
        if not query_by_platform:
            return StandardizedResponse(success=False, status_code=404,
                                        message='OOPS! There is no game with this platform')
        serializer = DataSalesSerializer(query_by_platform, many=True)
        return StandardizedResponse(success=True, status_code=200, data=serializer.data,
                                    message='The games with requested platform are found successfully')
