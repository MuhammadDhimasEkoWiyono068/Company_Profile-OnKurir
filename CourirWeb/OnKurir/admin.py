from django.contrib import admin
from .models import Beranda, Keunggulan, TentangKami, Tim

# Menambahkan model Inline untuk Keunggulan
class KeunggulanInline(admin.TabularInline):
    model = Keunggulan
    extra = 1  # Menampilkan satu kolom tambahan kosong untuk tambah keunggulan baru

# Registrasikan Beranda dengan KeunggulanInline
class BerandaAdmin(admin.ModelAdmin):
    inlines = [KeunggulanInline]

# Inline untuk Tim
class TimInline(admin.TabularInline):
    model = Tim
    extra = 1  # Tambahkan satu kolom kosong untuk entri baru

# Admin untuk TentangKami
class TentangKamiAdmin(admin.ModelAdmin):
    inlines = [TimInline]

admin.site.register(Beranda, BerandaAdmin)
admin.site.register(TentangKami, TentangKamiAdmin)
