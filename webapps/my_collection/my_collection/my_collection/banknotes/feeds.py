from django.contrib.syndication.views import Feed
from my_collection.banknotes.models import BankNote
from django.utils.feedgenerator import Atom1Feed

class RssRecentBanknoteFeed(Feed):
	title = u'Banknotes | Recent BankNotes'
	link = '/banknotes/recent/'
	description = u'Recent Banknotes posted to My Collection'
	
	def items(self):
		return BankNote.objects.order_by('-id')[:10]
	
	def item_title(self, item):
		return item.title
	
	def item_description(self, item):
		return item.description

class AtomRecentBanknoteFeed(RssRecentBanknoteFeed):
    feed_type = Atom1Feed
    subtitle = RssRecentBanknoteFeed.description