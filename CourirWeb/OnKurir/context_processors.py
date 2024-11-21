from .models import FooterMedia, TentangKami, Galeri

def social_media_links(request):
    return {
        'medias': FooterMedia.objects.all(),
        'footer_TitleTentangKami': TentangKami.objects.first(),
        'footer_TitleVisiMisi': TentangKami.objects.first(),
        'footer_Tim': TentangKami.objects.first(),
        'footer_Galeri': Galeri.objects.first(),
    }
