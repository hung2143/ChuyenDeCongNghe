from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
import datetime
import asyncio
from .models import Article


# 1. Basic View class
class SimpleView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Hello from Class-Based View!</h1>")

# 2. TemplateView - Hiển thị template
class AboutView(TemplateView):
    template_name = "articles/about.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_time'] = datetime.datetime.now()
        return context

# 3. ListView - Hiển thị danh sách objects
class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_articles'] = Article.objects.count()
        return context

# 4. DetailView - Hiển thị chi tiết object
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

# 5. Class-based view với custom HTTP methods (theo docs)
class BookListView(ListView):
    model = Article  # Sử dụng Article thay vì Book model
    template_name = 'articles/book_list.html'

    def head(self, *args, **kwargs):
        try:
            last_article = self.get_queryset().latest("publication_date")
            response = HttpResponse(
                headers={
                    "Last-Modified": last_article.publication_date.strftime(
                        "%a, %d %b %Y %H:%M:%S GMT"
                    )
                },
            )
        except Article.DoesNotExist:
            response = HttpResponse()
        return response

# 6. Async Class-based view (theo docs)
class AsyncView(View):
    async def get(self, request, *args, **kwargs):
        # Perform io-blocking view logic using await
        await asyncio.sleep(1)
        return HttpResponse("Hello async world!")

# Giữ lại các view cũ để không bị lỗi URLs
def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html lang="en"><body>It is now %s.</body></html>' % now
    return HttpResponse(html)

def simple_view(request):
    return HttpResponse("<h1>Hello, Django Views!</h1>")

def view_with_parameter(request, name):
    return HttpResponse(f"<h1>Hello, {name}!</h1>")

async def async_current_datetime(request):
    now = datetime.datetime.now()
    html = '<html lang="en"><body>Async: It is now %s.</body></html>' % now
    return HttpResponse(html)

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