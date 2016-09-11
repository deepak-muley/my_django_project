from django.conf.urls.defaults import *
from my_collection import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('my_collection.views',
    #Landing page
    url(r'^$', 'landing_page', name='landing_page'),
    
    #user Home page
    # url(r'^userpage/$', redirect_to, {'url': '/user/' }),
    url(r'^user/(?P<user_name>\w+)/$', 'user_home', name='user_home'),
        
    #About and contact information    
    url(r'^about/$', 'about', name='about'),
    url(r'^contact/$', 'contact', name='contact'),
    url(r'^find_your_location/$', 'find_your_location', name='find_your_location'),
        
    #Scratch pads
    url(r'^scratch_pad/$', 'scratch_pad', name='scratch_pad'),
    url(r'^scratch_pad2/$', 'scratch_pad2', name='scratch_pad2'),    
)

urlpatterns += patterns('',
    #Static data
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += patterns('',
    url(r'^banknotes/', include('my_collection.banknotes.urls')),
    url(r'^accounts/', include('my_collection.accounts.urls')),
    
    # using django admin framework
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    # using django comments framework
    url(r'^comments/', include('django.contrib.comments.urls')),
    
    # using django sitemap framework
    # url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),    
)
