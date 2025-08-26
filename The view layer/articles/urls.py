from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')

app_name = "articles"

urlpatterns = [
    # Simple views theo documentation
    path("datetime/", views.current_datetime, name="current_datetime"),
    path("simple/", views.simple_view, name="simple"),
    path("hello/<str:name>/", views.view_with_parameter, name="hello"),
    path("async-datetime/", views.async_current_datetime, name="async_datetime"),
    
    # URL patterns cũ
    path("2003/", views.special_case_2003, name="special_case_2003"),
    path("<int:year>/", views.year_archive, name="year_archive"),
    path("<int:year>/<int:month>/", views.month_archive, name="month_archive"),
    path("<int:year>/<int:month>/<slug:slug>/", views.article_detail, name="article_detail"),
    path("custom/<yyyy:year>/", views.year_archive, name="custom_year_archive"),
    path("", views.IndexView.as_view(), name="index"),
    path("detail/<int:pk>/", views.DetailView.as_view(), name="detail"),
]