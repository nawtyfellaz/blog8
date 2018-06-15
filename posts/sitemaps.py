from django.contrib.sitemaps import sitemaps
from .models import Post

class PostSitemap(sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return Post.obkects.all()

    def lastmod(self, obj):
        return obj.pub_date