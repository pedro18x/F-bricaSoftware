
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Enfermagem_app.views import PacienteViewSet, EnfermeiroViewSet

router = routers.DefaultRouter()
router.register('pacientes', PacienteViewSet, basename='Pacientes')
router.register('enfermeiros', EnfermeiroViewSet, basename='Enfermeiros')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
