from django.db import models

#------------------- Beranda -------------------
class Beranda(models.Model):
    banner_beranda = models.ImageField(upload_to='beranda/banner/')
    title_beranda = models.CharField(max_length=255)
    deskripsi_beranda = models.TextField()
    gambar_beranda = models.ImageField(upload_to='beranda/gambar/')

    title_keunggulan = models.CharField(max_length=255)

    def __str__(self):
        return self.title_beranda

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