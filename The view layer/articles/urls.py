from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')

app_name = "articles"

urlpatterns = [
    
    path("cbv-simple/", views.SimpleView.as_view(), name="cbv_simple"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("list/", views.ArticleListView.as_view(), name="article_list"),
    path("article/<slug:slug>/", views.ArticleDetailView.as_view(), name="article_detail"),
    path("books/", views.BookListView.as_view(), name="book_list"),
    path("async-cbv/", views.AsyncView.as_view(), name="async_cbv"),
    
    
    path("datetime/", views.current_datetime, name="current_datetime"),
    path("simple/", views.simple_view, name="simple"),
    path("hello/<str:name>/", views.view_with_parameter, name="hello"),
    path("async-datetime/", views.async_current_datetime, name="async_datetime"),
    path("2003/", views.special_case_2003, name="special_case_2003"),
    path("<int:year>/", views.year_archive, name="year_archive"),
    path("<int:year>/<int:month>/", views.month_archive, name="month_archive"),
    path("<int:year>/<int:month>/<slug:slug>/", views.article_detail, name="article_detail_old"),
    path("custom/<yyyy:year>/", views.year_archive, name="custom_year_archive"),
    path("", views.IndexView.as_view(), name="index"),
    path("detail/<int:pk>/", views.DetailView.as_view(), name="detail"),
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # Global templates directory
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'articles.context_processors.site_info',  # Custom context processor
            ],
            'debug': True,  # Template debug mode
            'string_if_invalid': '[INVALID: %s]',  # Show invalid variables
        },
    },
]