from django.conf.urls import patterns, include, url
from django.contrib import admin
from basketball import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fantasy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^/', include(admin.site.urls)),
    url(r'^$', views.todays_date, name='todays_game')
)
