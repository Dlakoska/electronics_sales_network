from rest_framework.routers import DefaultRouter
from network.views import NetworkNodeViewSet, ProductViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'nodes', NetworkNodeViewSet)
router.register(r'products', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
