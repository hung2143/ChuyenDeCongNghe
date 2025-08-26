from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render

def special_case_2003(request):
    """View cho trường hợp đặc biệt năm 2003"""
    # Demo reverse URL
    year_url = reverse('articles:year_archive', args=[2024])
    return HttpResponse(f"Đây là trang đặc biệt cho năm 2003!<br>URL năm 2024: <a href='{year_url}'>{year_url}</a>")

def year_archive(request, year):
    """View hiển thị archive theo năm"""
    # Demo reverse với kwargs
    month_url = reverse('articles:month_archive', kwargs={'year': year, 'month': 12})
    return HttpResponse(f"Archive cho năm {year}<br>URL tháng 12: <a href='{month_url}'>{month_url}</a>")

def month_archive(request, year, month):
    """View hiển thị archive theo tháng và năm"""
    # Demo reverse với slug
    article_url = reverse('articles:article_detail', kwargs={
        'year': year, 
        'month': month, 
        'slug': 'sample-article'
    })
    return HttpResponse(f"Archive cho tháng {month}/{year}<br>URL bài viết mẫu: <a href='{article_url}'>{article_url}</a>")

def article_detail(request, year, month, slug):
    """View hiển thị chi tiết bài viết"""
    index_url = reverse('articles:index')
    return HttpResponse(f"Chi tiết bài viết: {slug} (tháng {month}/{year})<br>Về trang chủ: <a href='{index_url}'>{index_url}</a>")

# Views cho namespace
class IndexView:
    @staticmethod
    def as_view():
        def view(request):
            detail_url = reverse('articles:detail', kwargs={'pk': 1})
            return HttpResponse(f"Trang chủ Articles<br>Chi tiết bài viết 1: <a href='{detail_url}'>{detail_url}</a>")
        return view

class DetailView:
    @staticmethod
    def as_view():
        def view(request, pk):
            index_url = reverse('articles:index')
            return HttpResponse(f"Chi tiết bài viết ID: {pk}<br>Về trang chủ: <a href='{index_url}'>{index_url}</a>")
        return view