from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from toutiao.views import show_news

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spider_news.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^show_news/',show_news),
)
