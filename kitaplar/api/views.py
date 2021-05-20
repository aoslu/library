from rest_framework.generics import GenericAPIView #GENERICAPIVİEW İÇİNDE look_up_fields sayesinde pk olduğu için detail apiviewde yazmak zorunda kalmadık ve url ismini belirlediğimiz yer burası restful yapı
#from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework import generics

from kitaplar.api.serializers import KitapSerializer, YorumSerializer
from kitaplar.models import Kitap

class KitapListCreateAPIView(generics.ListCreateAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer

class KitapDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer

#   QUERYSET VE SERİALİZER CLASSI BELİRTTİK VE GERİ KALANI LİSTCREATEAPIVİEW YANİ CONCRETEVİEW HALLETTİ... GENERİCS YANINDAKİ LİSTCREATEAPI VİEW İN KAYNAK KODUNDAN GÖZLEMLENEBİLİR BİR YAPI=> CONCRETEVİEWS
# class KitapListCreateAPIView(ListModelMixin, CreateModelMixin ,GenericAPIView):
#     queryset = Kitap.objects.all()
#     serializer_class = KitapSerializer
#     #Listelemek
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     #Yaratabilmek
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)