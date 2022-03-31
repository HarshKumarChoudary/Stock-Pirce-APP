from rest_framework import serializers
from NSEStockPriceApp.models import Company, Securities, Series, Bhavcopy


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('symbol', 'name', 'isinnumber')


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('series')


class SecuritiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Securities
        fields = ('date', 'paidup', 'maketlot',
                  'facevalue', 'series_id', 'company_id')


class BhavcopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Bhavcopy
        fields = ('open', 'high', 'low', 'close', 'last', 'previousclose',
                  'totaltrdq', 'totaltrdv', 'time', 'trades', 'series_id', 'company_id')
