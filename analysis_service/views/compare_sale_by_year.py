from utils.response_handler import StandardizedResponse
from main_service.models.data_sales import DataSales
from main_service.serializers.data_sales import DataSalesSerializer
from rest_framework.views import APIView
from rest_framework.views import Response
from django.shortcuts import render
from django.views.generic import View
import random

class CompareSaleByYearView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'compare_sale_year_chart.html',kwargs)

class CompareSaleByYearChartData(APIView):
    authentication_classes = []
    permission_classes = []
    

    def get(self, request, start_year, end_year):
        end_year += 1
        # query the names
        query_data = DataSales.objects.filter(year__range=(start_year, end_year))
        if not query_data:
            return StandardizedResponse(success=False, status_code=404,
                                        message='OOPS! There is no game with this name')
        serializer = DataSalesSerializer(query_data, many=True).data

        # create the data
        labels = [i for i in range(start_year, end_year)]
        data = dict()
        for q in serializer:
            if q['year'] in data:
                data[q['year']] += q['global_sales']
            else:
                data[q['year']] = q['global_sales']
        data = dict(sorted(data.items()))
        default_items = [val for val in data.values()]

        number_of_colors = len(default_items)

        colors = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
                for i in range(number_of_colors)]

        data = {
                "labels": labels,
                "default": default_items,
                "colors" : colors
        }
        return Response(data)