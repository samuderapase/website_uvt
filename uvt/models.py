import django
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
from django import forms
from django.forms import ModelForm
import datetime

class Post(models.Model):	
    penulis = models.ForeignKey(User)
    judul = models.CharField(max_length=200)
    #body = tinymce_models.HTMLField("tulisan")
    body = models.TextField("tulisan")
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
		ordering = ['penulis', 'judul', 'body']
		verbose_name_plural = "Post"
	
    def __unicode__(self):
		return self.judul
		
class Kategori_Perpus(models.Model):
	kategori = models.CharField(max_length=30)
	jenis_buku = models.CharField(max_length=30)
	
	class Meta:
		verbose_name_plural = "Kategori_Perpustakaan"
		
	def __unicode__(self):
		return self.kategori
	
class Buku(models.Model):
	judul = models.CharField(max_length=100)
	penulis = models.CharField(max_length=100)
	kategori = models.ForeignKey(Kategori_Perpus)
	cover = models.ImageField(upload_to="media/images", blank=True, null=True)
	tentang = tinymce_models.HTMLField("Deskripsi")
	penerbit = models.CharField(max_length=50)
	tanggal_publikasi = models.DateField()
	
	class Meta:
		verbose_name_plural = "Buku"
	
	def __unicode__(self):
		return self.judul


class Kategori_App(models.Model):
    nama = models.CharField(max_length=50, unique=True)
    deskripsi = models.TextField(default='', blank=True)
    ordering = models.IntegerField(default=0)

    def __unicode__(self):
        return self.nama

    class Meta:
        ordering = ('ordering',)
        verbose_name_plural = 'Kategori_Aplikasi'

class Aplikasi(models.Model):
    kategori = models.ForeignKey('Kategori_App')
    nama = models.CharField(max_length=50, unique=True)
    developer = models.CharField(max_length=50, unique=True)
    deskripsi = models.TextField(default='', blank=True)
    url = models.URLField(verify_exists=False, null=True, blank=True)
    tanggal = models.DateField()
    ordering = models.IntegerField(default=0)

    def __unicode__(self):
        return self.nama

    class Meta:
        ordering = ('developer', 'ordering',)
        verbose_name_plural = 'Aplikasi'
        
       
class KontakForm(forms.Form):
	subjek = forms.CharField()
	pesan = forms.CharField()
	pengirim = forms.EmailField()
	cc_myself = forms.BooleanField(required=False)
	
	class Meta:
		verbose_name_plural = "Kontak"
	
	def __unicode__(self):
		return self.subjek

class Jadwal(models.Model):
	hari = models.CharField(max_length=50)
	jam = models.TimeField("Waktu")
	tanggal = models.DateField()
	materi = models.TextField("Materi Kuliah")
	dosen = models.CharField(max_length=100)
	keterangan = models.TextField()
	
	class Meta:
		verbose_name_plural = "Jadwal"
	
	def __unicode__(self):
		return self.hari
