from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('index/', views.index,name='index'),
    path('purchases/', views.purchases, name='purchases'),
    path('order/', views.order, name='order'),
    path('irrigation/<str:table>', views.irrigation, name='irrigation'),
    path('plantation/<str:table>', views.plantation, name='plantation'),
    path('vehicle/<str:table>', views.vehicle, name='vehicle'),
    path('addItem/<str:form_name>', views.addItem, name='addItem'),
    path('delete/<label>/item_<pk>', views.delete_entry, name='deletion'),
    path('supplier/', views.supplier, name='supplier'),
]
