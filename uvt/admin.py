from uvt.models import*
from django.contrib import admin
from uvt.models import Kategori_App, Aplikasi

class PostAdmin(admin.ModelAdmin):
	list_display = ['judul', 'penulis', 'created']
	search_fields = ['judul']
	js = ['tiny_mce/tiny_mce.js', 'js/textareas.js'] 
	
class Kategori_PerpusAdmin(admin.ModelAdmin):
	list_display = ['kategori', 'jenis_buku']
	
class BukuAdmin(admin.ModelAdmin):
	list_display = ['judul', 'penulis', 'kategori', 'penerbit', 'tanggal_publikasi']


#class Kategori_appAdmin(admin.ModelAdmin):
#	list_display = ['nama', deskripsi, 'ordering']
    
class AplikasiAdmin(admin.ModelAdmin):
	list_display = ('nama', 'kategori')
	list_filter = ['kategori']

class JadwalAdmin(admin.ModelAdmin):
	list_display = ['hari', 'jam', 'tanggal', 'materi', 'dosen', 'keterangan']

    
admin.site.register(Post, PostAdmin)	
admin.site.register(Kategori_Perpus, Kategori_PerpusAdmin)
admin.site.register(Buku, BukuAdmin)
admin.site.register(Kategori_App)
admin.site.register(Aplikasi, AplikasiAdmin)
admin.site.register(Jadwal, JadwalAdmin)
