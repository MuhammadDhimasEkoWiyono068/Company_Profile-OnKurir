from .models import FooterMedia

def social_media_links(request):
    return {
        'medias': FooterMedia.objects.all(),
    }
