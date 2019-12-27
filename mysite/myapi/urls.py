from django.urls import include, path
from rest_framework import routers
from . import views
#
routers = routers.DefaultRouter()
routers.register(r'heroes', views.HeroViewSet)
#
# this is URL part
urlpatterns = [
    path('',include(routers.urls)),
    path('api-auth/',include('rest_framework.urls',
                             namespace='rest_framework'))
]

#
# urlpatterns = [
#     path('heroes/', views.HeroViewSet)
# ]
#
#
