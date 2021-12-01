from utils.response_handler import StandardizedResponse
from main_service.models.data_sales import DataSales
from main_service.serializers.data_sales import DataSalesSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.views import Response
from django.shortcuts import render
from django.views.generic import View
import json
import random


class CompareGamesView(View):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return render(request, 'compare_games_charts.html', kwargs)


class CompareGamesChartData(APIView):
    authentication_classes = []
    permission_classes = (IsAuthenticated,)

    def get(self, request, name1, name2):
        # query the names
        query_name1 = DataSales.objects.filter(name=name1)
        if not query_name1:
            return StandardizedResponse(success=False, status_code=404,
                                        message='OOPS! There is no game with this name')
        serializer1 = DataSalesSerializer(query_name1, many=True).data
        query_name2 = DataSales.objects.filter(name=name2)
        if not query_name2:
            return StandardizedResponse(success=False, status_code=404,
                                        message='OOPS! There is no game with this name')
        serializer2 = DataSalesSerializer(query_name2, many=True).data

        # create the data
        number_of_colors = 5

        colors = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
                  for i in range(number_of_colors)]

        backgroundColor = {
            "NA_sales": colors[0],
            "EU_sales": colors[1],
            "JP_sales": colors[2],
            "other_sales": colors[3],
            "global_sales": colors[4],
        }
        labels = [name1, name2]
        data = {"NA_sales": [], "EU_sales": [], "JP_sales": [], "other_sales": [], "global_sales": []}
        for k in data.keys():
            values = []
            values.append(serializer1[0][k])
            values.append(serializer2[0][k])
            data[k] = values
        default_items = []
        for k in data.keys():
            item = {}
            item['label'] = k
            item['data'] = data[k]
            item['backgroundColor'] = backgroundColor[k]
            default_items.append(item)
        default_items = json.dumps(default_items)
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)
