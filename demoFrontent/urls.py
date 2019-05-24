from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

# Path master ("home/")

app_name = 'demoFrontent'

urlpatterns = [
    url(r'^table/demo$', views.list_table),
    url(r'^demo$', views.demo),
    url(r'^copy-to-clipboard$', views.copy_to_clipboard),
    url(r'^notification$', views.notification),
    url(r'^select2-single$', views.select2_single),
    url(r'^dragable$', views.dragable),
    url(r'^spinner$', views.spinner),
    url(r'^chart$', views.chart),
    url(r'^demo-sales-setting$', views.demo_sales_setting),
    url(r'^ajax-get-form-sale-setting$', views.ajax_get_form_sale_setting),
    url(r'^contact/ajax-refresh-list-Oracle$', views.ajax_refresh_list_Oracle, name='ajax_refresh_list_Oracle'),
]
