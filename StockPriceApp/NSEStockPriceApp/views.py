from http.client import REQUEST_HEADER_FIELDS_TOO_LARGE
from json import JSONDecoder
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from NSEStockPriceApp.models import Company, Securities, Series, Bhavcopy
from NSEStockPriceApp.serializers import CompanySerializer, SecuritiesSerializer, SeriesSerializer
from NSEStockPriceApp.serializers import BhavcopySerializer
from django.shortcuts import render


def index(request):
    allseries = Series.objects.all()
    # print(allseries)
    ls = []
    for series in allseries:
        ls.append(series)
    options = []
    for x in ls:
        options.append(x.series)
    return render(request, "index.html", {'options': options})


@csrf_exempt
def output(request):
    # if request.method == 'GET':
    #     print(request.data)
    if request.method == 'POST':
        ser = request.POST.get('serie')
        sym = request.POST.get('symbol')
        # print(ser)
        comp_details = Company.objects.filter(symbol=sym)
        # print(comp_details)
        ser_details = Series.objects.filter(series=ser)
        fulldata = {}
        security_details = Securities.objects.filter(
            company_id=comp_details[0].id, series_id=ser_details[0].id)
        print(security_details.values()[0])
        bhavcopy_details = Bhavcopy.objects.filter(
            company_id=comp_details[0].id, series_id=ser_details[0].id)

        print(bhavcopy_details.values()[0])
        return render(request, 'output.html', {'security': security_details.values()[0], 'bhavcopy': bhavcopy_details.values()[0]})
    else:
        return render(request, "index.html")


@ csrf_exempt
def display(request):
    comp_data = Company.objects.all()
    comp_serial_data = CompanySerializer(data=comp_data)
    # return ValuesQuerySet object
    result = comp_serial_data.objects.values()
    comp = [entry for entry in result]
    if comp.is_valid():
        return JsonResponse(comp, safe=False)

    return JsonResponse(comp_serial_data.errors, safe=False)


class CompanyViewSet(viewsets.ModelViewSet):

    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer


class BhavcopyViewSet(viewsets.ModelViewSet):
    queryset = Bhavcopy.objects.all()
    serializer_class = BhavcopySerializer


class SecuritiesViewSet(viewsets.ModelViewSet):
    queryset = Securities.objects.all()

    serializer_class = SecuritiesSerializer
