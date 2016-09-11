from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from my_collection.banknotes.feeds import RssRecentBanknoteFeed, AtomRecentBanknoteFeed
from my_collection.banknotes.models import BankNote
from my_collection import settings

# Make sure you add the feeds dict before
# the urlpatterns object.
#feeds = {
#         'recent': RecentBankNotes
#}

urlpatterns = patterns('my_collection.banknotes.views',

   # banknotes by user
   url(r'^user/(?P<user_name>\w+)/$', 'get_banknotes', name='get_banknotes'),
   # banknotes collage by user
   url(r'^user/(?P<user_name>\w+)/collage/$', 'show_banknote_collage', name='show_banknote_collage'),
   # banknotes galleria by user
   url(r'^user/(?P<user_name>\w+)/galleria/$', 'show_banknote_galleria', name='show_banknote_galleria'),

   # banknotes by user by page   
   url(r'^user/(?P<user_name>\w+)/(?P<page_num>[0-9]+)/$', 'get_banknotes', name='get_banknotes'),
   
   # banknotes by user and tag
   url(r'^user/(?P<user_name>\w+)/tag/(?P<tag_name>[-\s\w]+)/$', 'get_banknotes', name='get_banknotes'),
   # banknotes by user and tag and page
   url(r'^user/(?P<user_name>\w+)/tag/(?P<tag_name>[-\s\w]+)/(?P<page_num>[0-9]+)/$', 'get_banknotes', name='get_banknotes'),

   # banknotes by tag only (future requirement)
   # url(r'^tag/([^\s]+)/$', 'banknotes_by_tag', name='banknotes_by_tag'),
      
   # details
   url(r'^(?P<pk>\d+)/details/$', 
        DetailView.as_view(
          model=BankNote,
          template_name='banknotes/banknote_details.html'),
          name='banknote_details'),
   
   # Statistics
   url(r'^stats/$', 'show_statistics', name='show_statistics'),
   url(r'^stats_by_country/$', 'show_country_statistics', name='show_country_statistics'),
   url(r'^stats_by_bank/$', 'show_bank_statistics', name='show_bank_statistics'),
   url(r'^stats_by_mint/$', 'show_mint_statistics', name='show_mint_statistics'),
   url(r'^stats_by_currency_unit/$', 'show_currency_unit_statistics', name='show_currency_unit_statistics'),
   
   #url(r'^save/$', 'save_banknote', { 'SSL': settings.ENABLE_SSL }, name='save_banknote'),
)

urlpatterns += patterns('',
   # Feeds
   #url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
   url(r'^recent/rss/$', RssRecentBanknoteFeed()),
   url(r'^recent/atom/$', AtomRecentBanknoteFeed()),   
)

