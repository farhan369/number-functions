from django.urls import path
from . import views
urlpatterns = [

    path('',views.indexpage),
    path('print',views.print),
    path('select',views.select),
    path('calculate',views.calculate)
]