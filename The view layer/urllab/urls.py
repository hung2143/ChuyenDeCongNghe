from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Include articles URLs theo documentation
    path('articles/', include('articles.urls')),
    
    # Thêm namespace examples theo documentation
    path('author-polls/', include('articles.urls', namespace='author-polls')),
    path('publisher-polls/', include('articles.urls', namespace='publisher-polls')),
]