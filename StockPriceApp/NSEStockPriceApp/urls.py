from django.urls import include, path

from rest_framework import routers

from NSEStockPriceApp.views import CompanyViewSet, SeriesViewSet, SecuritiesViewSet, BhavcopyViewSet
from NSEStockPriceApp import views

router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet)
router.register(r'series', SeriesViewSet)
router.register(r'securities', SecuritiesViewSet)
router.register(r'bhavcopy', BhavcopyViewSet)

urlpatterns = [
    path('', views.index),
    path('output', views.output),
    path('stock/', views.display),
    path('app/', include(router.urls)),
]
