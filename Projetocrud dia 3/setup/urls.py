from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from videogame_store.views import JogoViewSet, LojaViewSet

router = routers.DefaultRouter()
router.register('jogos', JogoViewSet, basename='Jogos')
router.register('lojas', LojaViewSet, basename='Loja')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
