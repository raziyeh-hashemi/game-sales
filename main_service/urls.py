from django.urls import path
from main_service.views.data_sales import AllDataSales
from main_service.views.detection_data_by_rank import GetDataByRank
from main_service.views.detection_data_by_platform import GetDataByPlatform
from main_service.views.detection_data_by_year import GetDataByYear

urlpatterns = [
    path('all_data/', AllDataSales.as_view(), name='get_all_data'),
    path('data_by_rank/<int:pk>/', GetDataByRank.as_view(), name='data_by_rank'),
    path('data_by_platform/<str:platform>/<int:pk>/', GetDataByPlatform.as_view(), name='data_by_platform'),
    path('data_by_year/<str:year>/<int:pk>/', GetDataByYear.as_view(), name='data_by_year'),
]
