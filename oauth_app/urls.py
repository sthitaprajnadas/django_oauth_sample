from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('index',views.index,name='anyname'),
    path('main', views.profile),
    path('logout',views.logout,name='anyname'),

   # url(r'index$', index)
]

