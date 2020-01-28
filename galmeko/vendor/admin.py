from django.contrib import admin
from .forms import CustomVendorCreationForm
from django.utils.html import format_html
from django.urls import path
from django.conf.urls import include, url
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.utils.translation import gettext, gettext_lazy as _
from django.utils.translation import ugettext_lazy
from user.admin import admin_site
from vendor.models import Vendor

class VendorAdmin(admin.ModelAdmin):
    form = CustomVendorCreationForm
    model = Vendor
    list_display = ('company_name','status')
    list_filter = ('status',)
    list_per_page = 5  

    fieldsets = (
        (None, {'fields': ('company_name','status')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('company_name','status')}
        ),
    )
    search_fields = ('company_name',)
    ordering = ('-id',)


    def save_vendor(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.user = request.user
            instance.save()
        formset.save_m2m()

admin_site.register(Vendor,VendorAdmin)
