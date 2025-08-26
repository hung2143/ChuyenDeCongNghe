from django.urls import path, register_converter
from . import views, converters

# Register custom converters
register_converter(converters.FourDigitYearConverter, 'yyyy')

app_name = "articles"

urlpatterns = [
    # Basic patterns theo documentation
    path("2003/", views.special_case_2003, name="special_case_2003"),
    path("<int:year>/", views.year_archive, name="year_archive"),
    path("<int:year>/<int:month>/", views.month_archive, name="month_archive"),
    path("<int:year>/<int:month>/<slug:slug>/", views.article_detail, name="article_detail"),
    
    # Custom converter example
    path("custom/<yyyy:year>/", views.year_archive, name="custom_year_archive"),
    
    # Namespace examples  
    path("", views.IndexView.as_view(), name="index"),
    path("detail/<int:pk>/", views.DetailView.as_view(), name="detail"),
]