from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('newsletter.views',

    url (r'^admin/newsletter/subscription/download/csv/$', 
        view='generate_csv',
        name='download_csv',
    ),
    
    url (r'^$', 
        view='subscribe_detail',
        name='subscribe_detail',
    ),

)
