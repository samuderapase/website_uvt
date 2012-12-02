# -*- coding: utf-8 -*- 

from django.db import models
import datetime
import simplejson
import pycurl
import StringIO
import re

# Create your models here.

class Category(models.Model):
  title = models.CharField(max_length=256, verbose_name='Judul')
  description = models.TextField(verbose_name='Deskripsi', blank=True)
  
  class Meta:
	  verbose_name_plural = "Kategori"
	  
  def __unicode__(self):
    return self.title

class Publisher(models.Model):
  name = models.CharField(max_length=256, verbose_name='Nama')
  link = models.URLField(max_length=256, blank=True, verbose_name="Link ke editor.")
  description = models.TextField(verbose_name='Deskripsi', blank=True)
  def __unicode__(self):
    return self.name

class Author(models.Model):
  surname = models.CharField(max_length=256, verbose_name='Nama')
  givenames = models.CharField(max_length=256, verbose_name='Pertama', blank=True)
  olid = models.CharField(max_length=24, blank=True, verbose_name='OLID')
  
  class Meta:
	  verbose_name_plural = "Penulis"
  def __unicode__(self):
    if self.givenames:
      return self.surname + ', ' + self.givenames
    else:
      return self.surname

class Book(models.Model):
  title = models.CharField(max_length=256, verbose_name='Judul')
  subtitle = models.CharField(max_length=256, blank=True, verbose_name='Sub-judul')
  description = models.TextField(verbose_name='Deskripsi', blank=True)
  isbn = models.CharField(max_length=24, blank=True, verbose_name='ISBN')
  oclc = models.CharField(max_length=24, blank=True, verbose_name='OCLC')
  lccn = models.CharField(max_length=24, blank=True, verbose_name='LCCN')
  olid = models.CharField(max_length=24, blank=True, verbose_name='OLID')
  olink = models.URLField(max_length=256, blank=True, verbose_name='Perpustakan Buka Link')
  cover = models.URLField(max_length=256, blank=True, verbose_name='Link ke gambar cover')
  ebook = models.URLField(max_length=256, blank=True, verbose_name='Link ke versi elektronik')
  language = models.CharField(max_length=3, choices= (
    ('MUL', 'Beberap/Bilingual'),
    ('INA', 'Indonesia'),
    ('Eng', 'Prancis'),
    ('Eng', 'Inggris'),
    ('Esp', 'Spanyol'),
    ('Tue', 'Lainnya'),
  ))
  category = models.ForeignKey(Category, blank=True, null=True, verbose_name='Bagian')
  author = models.ManyToManyField(Author, blank=True, null=True, verbose_name='Penulis')
  year = models.CharField(max_length=4, blank=True, verbose_name='Tahun') 
  publisher = models.ForeignKey(Publisher, blank=True, null=True, verbose_name="Penerbit")
  genre = models.CharField(max_length=256, blank=True, verbose_name='Genre')
  lost = models.BooleanField(default=False, verbose_name='Buku ini hilang')
  
  class Meta:
	  verbose_name_plural = "Buku"
	  
  def __unicode__(self):
    if self.subtitle:
      return self.title + ': ' + self.subtitle
    else:
      return self.title
  def not_available(self):
    if self.lost:
      return self.lost
    else:
      loans = self.loan_set.values('returned')
      result = False
      for line in loans:
        if line['returned'] is None:
          result = True
      return result
  def available(self):
    if self.not_available():
      return False
    else:
      return True
  def sanitize_isbn(self):
    if self.isbn:
      pattern = re.compile('[^0-9]')
      return pattern.sub('', self.isbn)
  def fetch_olrecord(self):
    if self.isbn:
      curlReq = pycurl.Curl()
      burl = 'http://openlibrary.org/api/books?bibkeys=ISBN:' + self.sanitize_isbn() + '&format=json&jscmd=data'
      curlReq.setopt(pycurl.URL, burl.__str__())
      curlReq.setopt(pycurl.FOLLOWLOCATION, 1)
      curlReq.setopt(pycurl.MAXREDIRS, 5)
      book = StringIO.StringIO()
      curlReq.setopt(pycurl.WRITEFUNCTION, book.write)
      curlReq.perform()
      book = StringIO.StringIO(book.getvalue())
      book = simplejson.load(book)
      return book[book.keys()[0]]

class Borrower(models.Model):
  name = models.CharField(max_length=256, verbose_name='Nama')
  email = models.EmailField(max_length=256, blank=True, verbose_name='Surel')
  phone = models.CharField(max_length=24, blank=True, verbose_name='Telepon')
  notes = models.TextField(blank=True, verbose_name='Notes')
  
  class Meta:
	  verbose_name_plural = "Peminjam"
  def __unicode__(self):
    return self.name

class Loan(models.Model):
  book = models.ForeignKey(Book, verbose_name='Buku')
  borrower = models.ForeignKey(Borrower, verbose_name='Peminjaman')
  borrowed = models.DateField(verbose_name="Tanggal pinjaman")
  due = models.DateField(verbose_name="Diharapkan tanggal pengembalian")
  returned = models.DateField(verbose_name="Tanggal pengembalian saat ini", blank=True, null=True)
  
  class Meta:
	  verbose_name_plural = "Pinjaman"
	  
  def __unicode__(self):
    return str(self.book) + ' (' + str(self.borrowed) + ' - ' + str(self.returned) + ')'
  def is_late(self):
    if self.returned is None:
      return self.due <= datetime.date.today()
    else:
      return False
      
