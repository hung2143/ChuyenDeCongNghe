from django.http import HttpResponse
import datetime
from django.shortcuts import render

# Simple view theo documentation
def current_datetime(request):
    """View trả về thời gian hiện tại"""
    now = datetime.datetime.now()
    html = '<html lang="en"><body>It is now %s.</body></html>' % now
    return HttpResponse(html)

def simple_view(request):
    """View đơn giản trả về HTML"""
    return HttpResponse("<h1>Hello, Django Views!</h1>")

def view_with_parameter(request, name):
    """View với parameter"""
    return HttpResponse(f"<h1>Hello, {name}!</h1>")

# Async view theo documentation
async def async_current_datetime(request):
    """Async view trả về thời gian hiện tại"""
    now = datetime.datetime.now()
    html = '<html lang="en"><body>Async: It is now %s.</body></html>' % now
    return HttpResponse(html)

# Giữ lại các view cũ cho URL patterns
def special_case_2003(request):
    return HttpResponse("Đây là trang đặc biệt cho năm 2003!")

def year_archive(request, year):
    return HttpResponse(f"Archive cho năm {year}")

def month_archive(request, year, month):
    return HttpResponse(f"Archive cho tháng {month}/{year}")

def article_detail(request, year, month, slug):
    return HttpResponse(f"Chi tiết bài viết: {slug} (tháng {month}/{year})")

class IndexView:
    @staticmethod
    def as_view():
        def view(request):
            return HttpResponse("Trang chủ Articles")
        return view

class DetailView:
    @staticmethod
    def as_view():
        def view(request, pk):
            return HttpResponse(f"Chi tiết bài viết ID: {pk}")
        return view

def template_view(request):
    """View sử dụng template"""
    context = {
        'current_time': datetime.datetime.now()
    }
    return render(request, 'articles/simple.html', context)