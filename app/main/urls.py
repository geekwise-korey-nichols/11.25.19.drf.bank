
from django.contrib import admin
from django.urls import path, include
from bank import views as bank_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'branch', bank_views.Branch_Viewset)
router.register(r'customer', bank_views.Customer_Viewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
