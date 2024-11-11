from django.shortcuts import render
from .models import Beranda, TentangKami

def beranda(request):
    beranda_data = Beranda.objects.first()  # Ambil data pertama (jika hanya ada satu data)
    return render(request, 'beranda.html', {'beranda': beranda_data})


def tentangkami(request):
    tentangkami_data = TentangKami.objects.first()
    return render(request, 'tentang_kami.html', {'tentangkami': tentangkami_data})
