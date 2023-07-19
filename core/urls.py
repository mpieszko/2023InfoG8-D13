from django.urls import path, include
from core import views  

#app_name = 'core'


urlpatterns = [
    path('', views.indexView, name = 'index'),

    # includes
    # path('noticias/', include('noticias.urls')),
    # path('usuarios/', include('usuarios.urls')),
]  