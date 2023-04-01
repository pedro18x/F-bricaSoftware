from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from videogame_store.views import BrinquedoViewSet, LojaViewSet, ClienteViewSet

router = routers.DefaultRouter()
router.register('Brinquedos', BrinquedoViewSet, basename='Brinquedo')
router.register('lojas', LojaViewSet, basename='Loja')
router.register('clientes', ClienteViewSet, basename='Cliente')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
