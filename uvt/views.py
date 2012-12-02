from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from models import *
from django.core.urlresolvers import reverse
from django.conf import settings
from django.template.context import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def index(request):
	return render_to_response('base.html', locals())
	
def artikel(request):
	return render_to_response('artikel.html', locals())

def tutorial(request):
    posts = Post.objects.all().order_by("-created")
    paginator = Paginator(posts, 2)

    try: 
		page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response("list.html", dict(posts=posts, user=request.user))

def post(request, pk):
    post = Post.objects.get(pk=int(pk))
    comments = Comment.objects.filter(post=post)
    d = dict(post=post, comments=comments, form=CommentForm(), user=request.user)
    d.update(csrf(request))
    return render_to_response("post.html", locals())


def perpustakaan(request):
	perpustakaan = Buku.objects.all()
	paginator = Paginator(perpustakaan, 7)
	
	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1
	
	try:
		fp = paginator.page(page)
	except (EmptyPage, InvalidPage):
		fp = paginator.page(paginator, num_pages)
			
	return render_to_response('perputakaan.html', {'perpustakaan':fp}) 


def aplikasi(request):
	aplikasi = Aplikasi.objects.all().order_by("-tanggal")
	paginator = Paginator(aplikasi, 5)
	
	try:
		page = int(request.GET.get("page", '1'))
	except ValueError: page = 1
	
	try:
		aplikasi = paginator.page(page)
	except (InvalidPage, EmptyPage):
		aplikasi = paginator.page(paginator.num_pages)
	return render_to_response('aplikasi/list.html', dict(aplikasi=aplikasi, user=request.user))
	
def aplikasi_app(request, pk):
    aplikasi = Aplikasi.objects.get(pk=int(pk))
    comments = Comment.objects.filter(aplikasi=aplikasi)
    d = dict(aplikasi=aplikasi, comments=comments, form=CommentForm(), user=request.user)
    d.update(csrf(request))
    return render_to_response("aplikasi/aplikasi.html", locals())

def kategori(request):
	kategori = Kategori_App.objects.all()
	return render_to_response('aplikasi/kategori.html')

def jadwal(request):
	jadwal = Jadwal.objects.all()
	return render_to_response('jadwal.html', locals())

def kontak(request):
	if request.method == 'POST':
		form = KontakForm(request.POST)
		if form.is_valid():
			subjek = form.cleaned_data['subjek']
			pesan = form.cleaned_data['pesan']
			pengirim = form.cleaned_data['pengirim']
			cc_myself = form.cleaned_data['cc_myself']
			
			penerima = ['x@gmail.com']
			if cc_myself:
				penerima.append(pengirim)
			from django.core.mail import send_mail
			send_mail(subjek, pesan, pengirim, penerima)
			return HttpResponseRedirect('/thanks/')
	else:
		form = KontakForm()
	
	return render(request, 'kontak.html',{
	     'form': form,
	})
	
