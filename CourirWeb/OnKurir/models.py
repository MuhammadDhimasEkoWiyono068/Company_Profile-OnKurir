from django.db import models

#------------------- Beranda -------------------
class Beranda(models.Model):
    title_beranda = models.CharField(max_length=255)
    deskripsi_beranda = models.TextField()
    gambar_beranda = models.ImageField(upload_to='beranda/gambar/')

    title_keunggulan = models.CharField(max_length=255)

    def __str__(self):
        return self.title_beranda

class Carousel(models.Model):
    beranda = models.ForeignKey(Beranda, related_name='carousel', on_delete=models.CASCADE)
    banner_beranda = models.ImageField(upload_to='beranda/banner/')
    
    def __str__(self):
        return f"Carousel {self.id}"

class Keunggulan(models.Model):
    beranda = models.ForeignKey(Beranda, related_name='keunggulan', on_delete=models.CASCADE)
    gambar_keunggulan = models.ImageField(upload_to='beranda/keunggulan/')
    title_Isikeunggulan = models.CharField(max_length=255)
    deskripsi_keunggulan = models.TextField()

    def __str__(self):
        return self.title_Isikeunggulan
    



#------------------- Tentang Kami -------------------
class TentangKami(models.Model):
    banner_TentangKami = models.ImageField(upload_to='TentangKami/banner/')
    title_TentangKami = models.CharField(max_length=255)
    deskripsi_TentangKami = models.TextField()
    gambar_TentangKami = models.ImageField(upload_to='TentangKami/gambar/')

    title_VisiMisi = models.CharField(max_length=255)
    deskripsi_VisiMisi = models.TextField()

    title_tim = models.CharField(max_length=255)

    def __str__(self):
        return self.title_TentangKami
    
class Tim(models.Model):
    tentangkami = models.ForeignKey(TentangKami, related_name='tim', on_delete=models.CASCADE)
    gambar_tim = models.ImageField(upload_to='TentangKami/Tim/')
    nama_tim = models.CharField(max_length=255)
    jabatan_tim = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_tim




#------------------- Layanan -------------------
class Layanan(models.Model):
    title_layanan = models.CharField(max_length=255)
    title_carakerja = models.CharField(max_length=255)
    title_ProsesPengiriman = models.CharField(max_length=255)
    title_KebijakanKetentuan = models.CharField(max_length=255)


    def __str__(self):
        return self.title_layanan

class IsiLayanan(models.Model):
    layanan = models.ForeignKey(Layanan, related_name='isi_layanan', on_delete=models.CASCADE)
    gambar_layanan = models.ImageField(upload_to='Layanan/')
    Jenis_layanan = models.CharField(max_length=255)
    deskripsi_layanan = models.TextField()
    proses_pengiriman = models.TextField()
    kebijakan_ketentuan = models.TextField()




#------------------- Galeri -------------------
class Galeri(models.Model):
    title_Galeri = models.CharField(max_length=255)

    def __str__(self):
        return self.title_Galeri
    
class IsiGaleri(models.Model):
    galeri = models.ForeignKey(Galeri, related_name='isi_galeri', on_delete=models.CASCADE)
    gambar_galeri = models.ImageField(upload_to='Galeri/')

    def __str__(self):
        return f"IsiGaleri {self.id}"

#------------------- Blog -------------------
class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0) 
    
    def __str__(self):
        return self.title