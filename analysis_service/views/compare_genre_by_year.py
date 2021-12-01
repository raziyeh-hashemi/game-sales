from utils.response_handler import StandardizedResponse
from main_service.models.data_sales import DataSales
from main_service.serializers.data_sales import DataSalesSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.views import Response
from django.shortcuts import render
from django.views.generic import View
import random
import json


class CompareGenreByYearView(View):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return render(request, 'compare_genre_by_year_char.html', kwargs)


class CompareGenreByYearChartData(APIView):
    permission_classes = (IsAuthenticated,)

    authentication_classes = []
    permission_classes = []

    def get(self, request, start_year, end_year):
        # query the names
        query_data = DataSales.objects.filter(year__range=(start_year, end_year))
        if not query_data:
            return StandardizedResponse(success=False, status_code=404,
                                        message='OOPS! There is no game with this name')

        serializer = DataSalesSerializer(query_data, many=True).data
        # create the data

        # sales per genre
        data = dict()
        for q in serializer:
            if q['genre'] in data:
                data[q['genre']] += q['global_sales']
            else:
                data[q['genre']] = q['global_sales']

        # labels
        labels = [i for i in data.keys()]

        # data
        default_items = [i for i in data.values()]

        number_of_colors = len(labels)

        colors = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
                  for i in range(number_of_colors)]

        label = str(start_year) + " to " + str(end_year)

        data = {
            "labels": labels,
            "default": default_items,
            "colors": colors,
            "label": label
        }
        return Response(data)
