from django import template
from django.contrib.flatpages.models import FlatPage
from my_collection.banknotes.models import BankNote

register = template.Library()

@register.inclusion_tag("tags/footer.html")
def footer_links():
    flatpage_list = FlatPage.objects.all()
    return {'flatpage_list': flatpage_list }

#===============================================================================
# @register.inclusion_tag("banknotes/banknote_list.html")
# def banknote_list():
#    banknote_list = BankNote.objects.all()
#    return {'banknote_list': banknote_list }
#===============================================================================