import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
import csv
import sys

from my_collection.banknotes.models import Country, CurrencyInfo, Bank, BankNote, Mint

def run():
    with open( 'scripts/collection_countries.csv', "rb" ) as theFile:
        reader = csv.DictReader( theFile )
        for line in reader:
            # line is { 'workers': 'w0', 'constant': 7.334, 'age': -1.406, ... }
            # e.g. print( line[ 'workers' ] ) yields 'w0'
            # print line
            try:
                try:
                    country = Country.objects.get(name=line['country_name'])
                    print 'country %s already exists hence skipping adding it again' % line['country_name']
                except Country.DoesNotExist:
                    print 'country %s does not exist hence adding' % line['country_name']                    
                    country = Country()
                    country.name = line['country_name']
                    country.url = line['country_wiki_url']
                    country.is_active = True
                    country.description = line['country_desc']
                    #country.created_at = datetime.datetime(2012, 5, 7, 10, 53, 26, 750000)
                    #country.updated_at = datetime.datetime(2012, 5, 7, 10, 53, 26, 750000)
                    country.save()
                    print 'Added country %s' % line['country_name']                    
            except Exception as e:
                print 'exception details: %s' % e

    with open( 'scripts/collection_mints.csv', "rb" ) as theFile:
        reader = csv.DictReader( theFile )
        for line in reader:
            # line is { 'workers': 'w0', 'constant': 7.334, 'age': -1.406, ... }
            # e.g. print( line[ 'workers' ] ) yields 'w0'
            # print line
            try:
                try:
                    mint = Mint.objects.get(name=line['mint_name'])
                    print 'mint %s already exist hence skipping' % line['mint_name']
                    continue
                except Mint.DoesNotExist:
                    print 'mint %s does not exist hence adding' % line['mint_name']
                    
                    mint = Mint()
                    try:
                        country = Country.objects.get(name=line['mint_country'])
                    except Country.DoesNotExist:
                        print 'country %s does not exist in Contry table hence cannot add mint %s' % line['mint_country'], line['mint_name']
                        sys.exit(-1)
                    mint.name = line['mint_name']
                    mint.country = country
                    mint.url = line['mint_wiki_url']
                    mint.is_active = True
                    mint.description = line['mint_desc']
                    #mint.created_at = datetime.datetime(2012, 5, 7, 10, 53, 39, 671000)
                    #mint.updated_at = datetime.datetime(2012, 5, 7, 10, 53, 39, 671000)
                    mint.save()
                    print 'Added mint %s' % line['mint_name']                
            except Exception as e:
                print 'exception details: %s' % e
                
    with open( 'scripts/collection_banks.csv', "rb" ) as theFile:
        reader = csv.DictReader( theFile )
        for line in reader:
            # line is { 'workers': 'w0', 'constant': 7.334, 'age': -1.406, ... }
            # e.g. print( line[ 'workers' ] ) yields 'w0'
            # print line
            try:
                try:
                    bank = Bank.objects.get(name=line['bank_name'])
                    print 'bank %s already exist hence skipping' % line['bank_name']
                    continue
                except Bank.DoesNotExist:
                    print 'bank %s does not exist hence adding' % line['bank_name']

                    bank = Bank()                
                    bank.name = line['bank_name']
                    try:
                        country = Country.objects.get(name=line['bank_country'])
                    except Country.DoesNotExist:
                        print 'country %s does not exist in Contry table hence cannot add bank %s' % line['bank_country'], line['bank_name']
                        sys.exit(-1)
                    bank.country = country
                    bank.url = line['bank_wiki_url']
                    bank.is_active = True
                    bank.description = line['bank_desc']
                    #bank.created_at = datetime.datetime(2012, 5, 7, 10, 53, 29, 593000)
                    #bank.updated_at = datetime.datetime(2012, 5, 7, 10, 53, 29, 593000)
                    bank.save()
                    print 'Added bank %s' % line['bank_name']                
            except Exception as e:
                print 'exception details: %s' % e

    with open( 'scripts/collection_currency_units.csv', "rb" ) as theFile:
        reader = csv.DictReader( theFile )
        for line in reader:
            # line is { 'workers': 'w0', 'constant': 7.334, 'age': -1.406, ... }
            # e.g. print( line[ 'workers' ] ) yields 'w0'
            # print line
            try:
                try:
                    currency_info = CurrencyInfo.objects.get(unit=line['currency_unit_name'])
                    print 'currency info %s - %s - %s - %s already exist hence skipping' % (line['currency_country'], line['currency_iso_4217_code'], line['currency_symbol'], line['currency_unit_name'])
                    continue
                except CurrencyInfo.DoesNotExist:
                    print 'currency info %s - %s - %s - %s does not exist hence adding' % (line['currency_country'], line['currency_iso_4217_code'], line['currency_symbol'], line['currency_unit_name'])
                    
                    currency_info = CurrencyInfo()
                    try:
                        country = Country.objects.get(name=line['currency_country'])
                    except Country.DoesNotExist:
                        print 'country %s does not exist in Contry table hence cannot add currency info %s - %s - %s' % (line['currency_country'], line['currency_iso_4217_code'], line['currency_symbol'], line['currency_unit_name'])
                        sys.exit(-1)
                    
                    currency_info.country = country
                    currency_info.code = line['currency_iso_4217_code']
                    currency_info.symbol = line['currency_symbol']
                    currency_info.unit = line['currency_unit_name']
                    if line['currency_unit_name'] == 'FALSE':
                        currency_info.is_subunit = False
                    else:
                        currency_info.is_subunit = True
                    currency_info.url = line['currency_wiki_url']
                    currency_info.is_active = True
                    currency_info.description = line['currency_desc']
                    #currency_info.created_at = datetime.datetime(2012, 5, 7, 10, 54, 19, 875000)
                    #currency_info.updated_at = datetime.datetime(2012, 5, 7, 10, 54, 19, 875000)
                    currency_info.save()
                    print 'Added currency unit info %s - %s - %s - %s' % (line['currency_country'], line['currency_iso_4217_code'], line['currency_symbol'], line['currency_unit_name'])
            except Exception as e:
                print 'exception details: %s' % e

    with open( 'scripts/collection_banknotes.csv', "rb" ) as theFile:
        reader = csv.DictReader( theFile )
        for line in reader:
            # line is { 'workers': 'w0', 'constant': 7.334, 'age': -1.406, ... }
            # e.g. print( line[ 'workers' ] ) yields 'w0'
            # print line
            try:
                banknote = BankNote()
                
                try:
                    bank = Bank.objects.get(name=line['bank'])
                except Bank.DoesNotExist:
                    print 'bank %s does not exist hence cannot add banknote' % line['bank']
                    sys.exit(-1)
                banknote.bank = bank
                
                try:
                    mint = Mint.objects.get(name=line['mint'])
                except Mint.DoesNotExist:
                    print 'mint %s does not exist hence cannot add banknote' % line['mint']
                    sys.exit(-1)
                banknote.mint = mint
                
                try:
                    currency_info = CurrencyInfo.objects.get(unit=line['unit'])
                except CurrencyInfo.DoesNotExist:
                    print 'currency info %s does not exist hence cannot add this banknote' % (line['unit'])
                    sys.exit(-1)
                banknote.unit = currency_info
                
                banknote.value = line['value']
                banknote.signed_by = line['signed_by']
                banknote.series = line['series']
                banknote.serial_number = line['serial_number']
                banknote.material = line['material']
                banknote.obverse_img = u'photos/%s' % line['obverse_img']
                banknote.obverse_desc = line['obverse_desc']
                banknote.reverse_img = u'photos/%s' % line['reverse_img']
                banknote.reverse_desc = line['reverse_desc']
                banknote.grade = line['grade']
                banknote.status = line['status']
                banknote.main_color = line['main_color']
                
                #TODO
                banknote.issue_date = datetime.date(2012, 5, 7)
                #date is going to be in format MM/DD/YYYY
                
                banknote.dimensions = line['dimensions']
                banknote.url = line['wiki_url']
                banknote.tags_input = line['tags']
                banknote.is_active = True
                banknote.description = line['desc']
                #banknote.created_at = datetime.datetime(2012, 5, 7, 10, 54, 33, 562000)
                #banknote.updated_at = datetime.datetime(2012, 5, 7, 10, 54, 33, 562000)
                banknote.user = User.objects.get(id=1)
                
                banknote.save()
                print 'Added banknote'
            except Exception as e:
                print 'exception details: %s' % e

#if __name__ == "__main__":
#    run()
