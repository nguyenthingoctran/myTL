from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

# Path master ("home/")

app_name = 'demoFrontent'

urlpatterns = [
    url(r'^table/demo$', views.list_table),
    url(r'^copy-to-clipboard$', views.copy_to_clipboard),
    url(r'^notification$', views.notification),
    url(r'^select2-single$', views.select2_single),
    url(r'^dragable$', views.dragable),
]
