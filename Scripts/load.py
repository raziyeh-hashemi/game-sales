import os
import csv
import pandas as pd
from main_service.models.data_sales import DataSales

def run():
    # file = open('/home/leila/Desktop/GameSale/game-sales/vgsales.csv')
    # read_file = csv.reader(file)
    read_file = pd.read_csv('vgsales.csv', keep_default_na=False)
    read_file['Year'] = read_file['Year'].replace(['N/A'], 0)
    DataSales.objects.all().delete()
    
    count = 1
    for index, record in read_file.iterrows():
        # print(count)
        DataSales.objects.create(rank=record['Rank'], name=record['Name'], platform=record['Platform'],
        year=record['Year'], genre=record['Genre'], publisher=record['Publisher'], NA_sales=record['NA_Sales'], 
        EU_sales=record['EU_Sales'], JP_sales=record['JP_Sales'], other_sales=record['Other_Sales'], global_sales= record['Global_Sales'])
        count += 1