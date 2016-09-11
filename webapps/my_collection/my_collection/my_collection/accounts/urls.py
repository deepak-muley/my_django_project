from django.conf.urls.defaults import patterns, include, url
from my_collection import settings

urlpatterns = patterns('my_collection.accounts.views',
    url(r'^register/$', 'register', 
        {'template_name': 'registration/register.html' , 'SSL': settings.ENABLE_SSL }, 'register'),
    url(r'^my_account/$', 'my_account', 
        {'template_name': 'registration/my_account.html'}, 'my_account'),
                       
    # Friends
    url(r'^friends/(\w+)/$', 'friends_page', name='friends_page'),
    url(r'^friend/add/$', 'friend_add', name='friend_add'),
    url(r'^friend/invite/$', 'friend_invite', name='friend_invite'),
    url(r'^friend/accept/(\w+)/$', 'friend_accept', name='friend_accept'),    
                       
)

urlpatterns += patterns('django.contrib.auth.views',
	url(r'^login/$', 'login', 
		{'template_name': 'registration/login.html', 'SSL': settings.ENABLE_SSL }, 'login'),
    url(r'^logout/$', 'logout', 
        {'template_name': 'registration/logged_out.html'}, 'logout'),
    url(r'^password_change/$', 'password_change', 
        {'template_name': 'registration/password_change_form.html', 'SSL': settings.ENABLE_SSL }, 'password_change'),
    url(r'^password_change/done/$', 'password_change_done', 
        {'template_name': 'registration/password_change_done.html'}, 'password_change_done'),
    url(r'^password_reset/$', 'password_reset', 
        {'template_name': 'registration/password_reset_form.html'}, 'password_reset'),
)

urlpatterns += patterns('',
    url(r'^', include('django.contrib.auth.urls')),                        
)
