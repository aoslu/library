from django.contrib import admin
from kitaplar.models import Kitap, Yorum
# Register your models here.

#class KitapAdmin(admin.ModelAdmin):
admin.site.register(Kitap)

#class YorumAdmin(admin.ModelAdmin):
admin.site.register(Yorum)