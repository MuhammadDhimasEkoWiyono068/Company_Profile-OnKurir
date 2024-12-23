from django.contrib import admin
from django.db import models
from django.utils.html import mark_safe
from markdownx.admin import MarkdownxModelAdmin
from .models import Beranda, Carousel, Keunggulan, TentangKami, Tim, Galeri, IsiGaleri, Layanan, IsiLayanan, Blog, FooterMedia, KontakKami, KontakList
from django import forms

#------------------- Beranda -------------------
class CarouselInline(admin.TabularInline):
    model = Carousel
    extra = 1  # Menampilkan satu kolom tambahan kosong untuk tambah gambar carousel baru
    fields = ['banner_beranda']  # Menampilkan hanya field 'image'

class KeunggulanInline(admin.TabularInline): # Menambahkan model Inline untuk Keunggulan
    model = Keunggulan
    extra = 1 

class BerandaAdmin(admin.ModelAdmin): # Registrasikan Beranda dengan KeunggulanInline
    inlines = [CarouselInline, KeunggulanInline]



#------------------- Tentang Kami -------------------
class TimInline(admin.TabularInline): # Inline untuk Tim
    model = Tim
    extra = 1 

class TentangKamiAdmin(admin.ModelAdmin): # Admin untuk TentangKami
    inlines = [TimInline]



#------------------- Layanan -------------------
class IsiLayananInline(admin.TabularInline):
    model = IsiLayanan
    extra = 1

class LayananAdmin(admin.ModelAdmin):
    inlines = [IsiLayananInline]
    # list_display = ('title_layanan',)



#------------------- Galeri -------------------
class IsiGaleriInline(admin.TabularInline):
    model = IsiGaleri
    extra = 1

class GaleriAdmin(admin.ModelAdmin):
    inlines = [IsiGaleriInline]  # Menambahkan IsiGaleriInline di dalam admin Galeri
    # list_display = ('title_Galeri',)  # Menampilkan title_Galeri di admin list view

#-------------------- Blog --------------------------
class BlogAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'date')
    
    


admin.site.register(Beranda, BerandaAdmin)
admin.site.register(TentangKami, TentangKamiAdmin)
admin.site.register(Layanan, LayananAdmin)
admin.site.register(Galeri, GaleriAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(FooterMedia)
admin.site.register(KontakKami)
admin.site.register(KontakList)