from utils.response_handler import StandardizedResponse
from main_service.models.data_sales import DataSales
from main_service.serializers.data_sales import DataSalesSerializer
from rest_framework.views import APIView
from rest_framework.views import Response
from django.shortcuts import render
from django.views.generic import View
import random
import json

class ComparePublisherByYearView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'compare_publisher_by_year_chart.html',kwargs)

class ComparePublisherByYearChartData(APIView):
    authentication_classes = []
    permission_classes = []
    

    def get(self, request,publisher1, publisher2, start_year, end_year):
        # query the names
        query_data = DataSales.objects.filter(year__range=(start_year, end_year))
        if not query_data:
            return StandardizedResponse(success=False, status_code=404,
                                        message='OOPS! There is no game with this name')
        query_publisher1 = query_data.filter(publisher=publisher1)
        if not query_publisher1:
            return StandardizedResponse(success=False, status_code=404,
                                        message='OOPS! There is no game with this name')

        serializer1 = DataSalesSerializer(query_publisher1, many=True).data


        query_publisher2 = query_data.filter(publisher=publisher2)
        if not query_publisher2:
            return StandardizedResponse(success=False, status_code=404,
                                        message='OOPS! There is no game with this name')
        serializer2 = DataSalesSerializer(query_publisher2, many=True).data
        # create the data

        # sales per year for publisher 1
        data_publisher1 = dict()
        for q in serializer1:
            if q['year'] in data_publisher1:
                data_publisher1[q['year']] += q['global_sales']
            else:
                data_publisher1[q['year']] = q['global_sales']
        data_publisher1 = dict(sorted(data_publisher1.items()))
        
        # sales per year for publisher 2
        data_publisher2 = dict()
        for q in serializer2:
            if q['year'] in data_publisher2:
                data_publisher2[q['year']] += q['global_sales']
            else:
                data_publisher2[q['year']] = q['global_sales']
        data_publisher2 = dict(sorted(data_publisher2.items()))
        
        # labels
        labels = [i for i in data_publisher1.keys()]

        # data
        default_items = []

        number_of_colors = 2

        colors = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
                for i in range(number_of_colors)]

        item1 = {'label': publisher1, 'data': [i for i in data_publisher1.values()], "fill": False, 
        'borderColor': colors[0], 'tension': 0.1}
        item2 = {'label': publisher2, 'data': [i for i in data_publisher2.values()], "fill": False, 
        'borderColor': colors[1], 'tension': 0.1}

        default_items.append(item1)
        default_items.append(item2)

        default_items = json.dumps(default_items)
        
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)