from django.contrib import admin

# Register your models here.
from NSEStockPriceApp.models import Company, Series, Securities, Bhavcopy


class CompanyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Company, CompanyAdmin)


class SeriesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Series, CompanyAdmin)


class SecuritiesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Securities, CompanyAdmin)


class BhavcopyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Bhavcopy, CompanyAdmin)
