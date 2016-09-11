print '---------'

import os, sys
from optparse import OptionParser

usage = "usage: %prog -s SETTINGS | --settings=SETTINGS"
parser = OptionParser(usage)
parser.add_option('-s', '--settings', dest='settings', metavar='SETTINGS',
                  help="The Django settings module to use")
(options, args) = parser.parse_args()
if not options.settings:
    parser.error("You must specify a settings module")

os.environ['DJANGO_SETTINGS_MODULE'] = options.settings

ppath="C:\\Documents and Settings\\dmuley\\Collectibles"
if ppath not in sys.path:
    sys.path.append(ppath)

from django.core.management import setup_environ
try:
    from my_collection import settings
except ImportError:
    print "You don't appear to have a settings file in this directory!"
    print "Please run this from inside a project directory"
    sys.exit()
    
setup_environ(settings)
print '---------'

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType
import csv

from my_collection.banknotes.models import Country, CurrencyUnit, Bank, BankNote, Mint

def run():
    with open( 'Currencies - My Collection.csv', "rb" ) as theFile:
        reader = csv.DictReader( theFile )
        for line in reader:
            # line is { 'workers': 'w0', 'constant': 7.334, 'age': -1.406, ... }
            # e.g. print( line[ 'workers' ] ) yields 'w0'
            # print line
            try:
                Country_1 = Country()
                Country_1.name = u'bbcccc'
                Country_1.url = u''
                Country_1.is_active = True
                Country_1.description = u''
                Country_1.created_at = datetime.datetime(2012, 5, 7, 10, 53, 26, 750000)
                Country_1.updated_at = datetime.datetime(2012, 5, 7, 10, 53, 26, 750000)
                print '4'
                Country_1.save()
                print '5'
            except Exception as e:
                print 'exception details: %s' % e

if __name__ == "__main__":
    run()