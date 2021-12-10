from rest_framework import serializers
from main_service.models.data_sales import DataSales


class DataSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSales
        fields = '__all__'
