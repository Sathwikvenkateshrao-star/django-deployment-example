from django.urls import path
from BasicApp import views

# TEMPLATE TAGGING

app_name = 'BasicApp'


urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other',views.other,name='other'),
]