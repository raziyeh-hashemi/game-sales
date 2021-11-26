from django.urls import path
from main_service.views.data_sales import AllDataSales
from main_service.views.detection_data_by_rank import GetDataByRank
from main_service.views.detection_data_by_platform import GetDataByPlatform
from main_service.views.detection_data_by_year import GetDataByYear
from main_service.views.detedtion_data_by_genre import GetDataByGenre
from main_service.views.the_best_games import GetBestData
from main_service.views.detection_games_greater_EU import GetGreaterEuroData

urlpatterns = [
    path('all_data/', AllDataSales.as_view(), name='get_all_data'),
    path('data_by_rank/<int:pk>/', GetDataByRank.as_view(), name='data_by_rank'),
    path('data_by_platform/<str:platform>/<int:pk>/', GetDataByPlatform.as_view(), name='data_by_platform'),
    path('data_by_year/<str:year>/<int:pk>/', GetDataByYear.as_view(), name='data_by_year'),
    path('data_by_genre/<str:genre>/<int:pk>/', GetDataByGenre.as_view(), name='data_by_genre'),
    path('best_games/<str:platform>/<str:year>/', GetBestData.as_view(), name='best_games'),
    path('data_by_greater_euro/', GetGreaterEuroData.as_view(), name='data_by_greater_euro'),
]
