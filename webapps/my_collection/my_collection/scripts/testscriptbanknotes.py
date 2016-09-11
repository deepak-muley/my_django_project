#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated, changes may be lost if you
# go and generate it again. It was generated with the following command:
# C:\Documents and Settings\dmuley\Collectibles\my_collection\manage.py dumpscript banknotes

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

def run():
    from my_collection.banknotes.models import Country

    Country_1 = Country()
    Country_1.name = u'bb'
    Country_1.url = u''
    Country_1.is_active = True
    Country_1.description = u''
    Country_1.created_at = datetime.datetime(2012, 5, 7, 10, 53, 26, 750000)
    Country_1.updated_at = datetime.datetime(2012, 5, 7, 10, 53, 26, 750000)
    Country_1.save()

    from my_collection.banknotes.models import CurrencyUnit

    CurrencyInfo_1 = CurrencyUnit()
    CurrencyInfo_1.country = Country_1
    CurrencyInfo_1.code = u'rr'
    CurrencyInfo_1.symbol = u'rrr'
    CurrencyInfo_1.unit = u'ttt'
    CurrencyInfo_1.is_subunit = False
    CurrencyInfo_1.url = u''
    CurrencyInfo_1.is_active = True
    CurrencyInfo_1.description = u''
    CurrencyInfo_1.created_at = datetime.datetime(2012, 5, 7, 10, 54, 19, 875000)
    CurrencyInfo_1.updated_at = datetime.datetime(2012, 5, 7, 10, 54, 19, 875000)
    CurrencyInfo_1.save()

    from my_collection.banknotes.models import Mint

    Mint_1 = Mint()
    Mint_1.name = u'nn'
    Mint_1.country = Country_1
    Mint_1.url = u''
    Mint_1.is_active = True
    Mint_1.description = u''
    Mint_1.created_at = datetime.datetime(2012, 5, 7, 10, 53, 39, 671000)
    Mint_1.updated_at = datetime.datetime(2012, 5, 7, 10, 53, 39, 671000)
    Mint_1.save()

    from my_collection.banknotes.models import Bank

    Bank_1 = Bank()
    Bank_1.name = u'bb'
    Bank_1.country = Country_1
    Bank_1.url = u''
    Bank_1.is_active = True
    Bank_1.description = u''
    Bank_1.created_at = datetime.datetime(2012, 5, 7, 10, 53, 29, 593000)
    Bank_1.updated_at = datetime.datetime(2012, 5, 7, 10, 53, 29, 593000)
    Bank_1.save()

    from my_collection.banknotes.models import BankNote

    BankNote_1 = BankNote()
    BankNote_1.bank = Bank_1
    BankNote_1.mint = Mint_1
    BankNote_1.unit = CurrencyInfo_1
    BankNote_1.value = 4
    BankNote_1.signed_by = u''
    BankNote_1.series = u''
    BankNote_1.serial_number = u''
    BankNote_1.material = u'Paper'
    BankNote_1.obverse_img = u'photos/2012/05/07/Newzeland-10-shillings-back.jpg'
    BankNote_1.obverse_desc = u''
    BankNote_1.reverse_img = u'photos/2012/05/07/Newzeland-10-shillings-front.jpg'
    BankNote_1.reverse_desc = u''
    BankNote_1.grade = u'UNC'
    BankNote_1.status = u'In-circulation'
    BankNote_1.main_color = u''
    BankNote_1.issue_date = datetime.date(2012, 5, 7)
    BankNote_1.dimensions = u''
    BankNote_1.url = u''
    BankNote_1.tags_input = u''
    BankNote_1.is_active = True
    BankNote_1.description = u''
    BankNote_1.created_at = datetime.datetime(2012, 5, 7, 10, 54, 33, 562000)
    BankNote_1.updated_at = datetime.datetime(2012, 5, 7, 10, 54, 33, 562000)
    BankNote_1.save()

    BankNote_1.user = User.objects.get(id=1)
    BankNote_1.save()

