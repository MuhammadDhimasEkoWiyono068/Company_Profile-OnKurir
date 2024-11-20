from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Beranda, TentangKami, Layanan, Galeri, Blog, KontakKami, KontakList
from .forms import CommentForm
from django.http import JsonResponse
from django.template.loader import render_to_string

def beranda(request):
    beranda_data = Beranda.objects.first()  # Ambil data pertama (jika hanya ada satu data)
    galeri_data = Galeri.objects.first()  # Ambil data galeri pertama
    gambar_list = galeri_data.isi_galeri.all()[:4]  # Ambil hanya 4 gambar pertama
    return render(request, 'beranda.html', {
        'beranda': beranda_data, 
        'galeri': galeri_data,
        'gambar_list': gambar_list
    })

def tentangkami(request):
    tentangkami_data = TentangKami.objects.first()
    return render(request, 'tentang_kami.html', {'tentangkami': tentangkami_data})

def layanan(request):
    layanan_data = Layanan.objects.first()
    return render(request, 'layanan.html', {'layanan': layanan_data})



def galeri(request):
    galeri_data = Galeri.objects.first()  # Ambil data galeri pertama
    gambar_list = galeri_data.isi_galeri.all()  # Ambil semua gambar dalam galeri

    # Paginasi: Batasi hanya 6 gambar per halaman
    paginator = Paginator(gambar_list, 9)
    page_number = request.GET.get('page')  # Ambil parameter halaman dari URL
    page_obj = paginator.get_page(page_number)

    return render(request, 'galeri.html', {'galeri': galeri_data, 'page_obj': page_obj})

def blog_list(request):
    # Get the filter type from the GET parameters
    filter_type = request.GET.get('filter', 'latest')  # Default filter is 'latest'

    # Fetch the blogs based on the filter
    if filter_type == 'popular':
        blogs = Blog.objects.order_by('-views')  # Or '-likes' if you're using likes for popularity
    else:
        blogs = Blog.objects.order_by('-date')

    # Pagination
    paginator = Paginator(blogs, 6)  # Show 6 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog_list.html', {'blogs': page_obj, 'filter': filter_type})

def blog_detailed(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.views += 1
    all_comments = blog.comments.all().order_by('-created_at')
    
    form = CommentForm()

    context = {
        'blog': blog,
        'comments': all_comments,
        'form': form,
    }
    return render(request, 'blog_detailed.html', context)

def kontak_kami(request):
    kontak_kami = KontakKami.objects.first()
    list_kontak = KontakList.objects.all()
    return render(request, 'kontak_kami.html', {'data' : kontak_kami, 'list' : list_kontak})