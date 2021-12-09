from django.urls import path
from main_service.views.data_sales import AllDataSales
from main_service.views.query_data_by_rank import GetDataByRank
from main_service.views.query_data_by_platform import GetDataByPlatform
from main_service.views.query_data_by_year import GetDataByYear
from main_service.views.query_data_by_genre import GetDataByGenre
from main_service.views.the_best_games import GetBestData
from main_service.views.query_games_greater_EU import GetGreaterEuroData
from main_service.views.search_by_name import SearchByName

urlpatterns = [
    path('all_data/', AllDataSales.as_view(), name='get_all_data'),
    path('search_by_rank/<int:pk>/', GetDataByRank.as_view(), name='search_by_rank'),
    path('search_by_platform/<str:platform>/<int:pk>/', GetDataByPlatform.as_view(), name='search_by_platform'),
    path('search_by_year/<str:year>/<int:pk>/', GetDataByYear.as_view(), name='search_by_year'),
    path('search_by_genre/<str:genre>/<int:pk>/', GetDataByGenre.as_view(), name='search_by_genre'),
    path('best_games/<str:platform>/<str:year>/', GetBestData.as_view(), name='best_games'),
    path('search_by_greater_euro/', GetGreaterEuroData.as_view(), name='search_by_greater_euro'),
    path('search_by_name/<str:name>/', SearchByName.as_view(), name='search_by_name'),
]
