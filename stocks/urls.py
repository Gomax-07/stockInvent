from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('Supplier', views.SupplierViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stocks.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))

    
 ]