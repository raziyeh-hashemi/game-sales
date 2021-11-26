from django.urls import path
from main_service.views.data_sales import AllDataSales

urlpatterns = [
    path('all_data/', AllDataSales.as_view(), name='get_all_data'),

]
