from django import forms
from my_collection.banknotes.models import Country, Bank, Mint, BankNote, CurrencyInfo 

class BanknoteSaveForm(forms.ModelForm):
    class Meta:
        model = BankNote
        # exclude = ('user',)

class BankSaveForm(forms.ModelForm):
    class Meta:
        model = Bank

class MintSaveForm(forms.ModelForm):
    class Meta:
        model = Mint

class BanknoteSaveForm(forms.ModelForm):
    class Meta:
        model = BankNote
        
class CurrencyInfoSaveForm(forms.ModelForm):
    class Meta:
        model = CurrencyInfo 
        