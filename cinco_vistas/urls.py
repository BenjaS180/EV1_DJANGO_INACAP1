from django.urls import path
from . import views


urlpatterns = [
    path('',views.home ,name = 'home'),
    path('campeones/',views.campeones, name='campeones'),
    path('items/',views.items, name='items'),
    path('plays/',views.plays, name='plays'),
]
