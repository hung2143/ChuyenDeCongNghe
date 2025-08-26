from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    
    class Meta:
        ordering = ['-publication_date']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('articles:article_detail', kwargs={'slug': self.slug})