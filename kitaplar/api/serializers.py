from rest_framework import serializers
from kitaplar.models import Kitap, Yorum
#from kitaplar.api.serializers import YorumSerializer

class YorumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yorum
        #fields = '__all__'
        exclude = ['kitap']
        read_only_fields = []

class KitapSerializer(serializers.ModelSerializer):
    yorumlar = YorumSerializer(many=True, read_only=True)
    class Meta:
        model = Kitap
        fields = '__all__'
