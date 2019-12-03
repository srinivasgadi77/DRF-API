from django.shortcuts import render

from rest_framework import viewsets

from .serializers import HeroSerializer
from .models import Hero

#
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

# #
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Hero
# from .serializers import HeroSerializer
#
# class HeroesList(APIView):
#
#
#     def get(self, request):
#         HName = Hero.objects.all()
#         serializer = HeroSerializer(HName, many=True)
#         return Response(serializer.data)
#
#     def post(self):
#         pass
