from django.urls import path, include

from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.index, name='index'),
    path('ice_cream/', include('ice_cream.urls', namespace='ice_cream'))
]
