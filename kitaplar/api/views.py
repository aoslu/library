from rest_framework.generics import GenericAPIView #GENERICAPIVİEW İÇİNDE look_up_fields sayesinde pk olduğu için detail apiviewde yazmak zorunda kalmadık ve url ismini belirlediğimiz yer burası restful yapı
#from rest_framework.mixins import ListModelMixin, CreateModelMixin    # CONCRETEVİEW YAKLAŞIMI SUPER CLASSLAR SAYESİNDE BUNU EKLEMEMİZE GEREK KALMADI

from rest_framework import generics

from kitaplar.api.serializers import KitapSerializer, YorumSerializer
from kitaplar.models import Kitap, Yorum
from rest_framework.generics import get_object_or_404
from rest_framework import permissions   #SAFE METHODLAR VERİ TABANINDA BİRDEĞİŞİKLİK YAPMAYAN METODLARDIR

class KitapListCreateAPIView(generics.ListCreateAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer

class KitapDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer

class YorumCreateAPIView(generics.CreateAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer

    def perform_create(self, serializer):   #SINIFIN İÇİNE YAZILAN FONXİYONLAR METOD OLARAK ADLANDIRILABİLİR
        kitap_pk = self.kwargs.get('kitap_pk')
        kitap = get_object_or_404(Kitap, pk=kitap_pk)
        serializer.save(kitap=kitap)

class YorumDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer


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