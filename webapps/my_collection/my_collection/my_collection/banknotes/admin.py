from my_collection.banknotes.models import BankNote, Country, Bank, CurrencyInfo, Mint 
from django.contrib import admin
from django.contrib.contenttypes import generic

class MintInline(admin.TabularInline):
    model = Mint

class MintAdmin(admin.ModelAdmin):
   pass


class CurrencyInfoInline(admin.TabularInline):
    model = CurrencyInfo

class CurrencyInfoAdmin(admin.ModelAdmin):
    pass


class BankInline(admin.TabularInline):
    model = Bank

class BankAdmin(admin.ModelAdmin):
    pass


class CountryInline(admin.TabularInline):
    model = Country

class CountryAdmin(admin.ModelAdmin):
    pass

class BankNoteAdmin(admin.ModelAdmin):
    #===========================================================================
    # list_display = ('denomination', 'grade')
    # list_filter = ['denomination', 'grade']
    # search_fields = ['denomination', 'grade']
    #===========================================================================
    pass

admin.site.register(Mint, MintAdmin)
admin.site.register(CurrencyInfo, CurrencyInfoAdmin)     
admin.site.register(Bank, BankAdmin)     
admin.site.register(Country, CountryAdmin)
admin.site.register(BankNote, BankNoteAdmin)
