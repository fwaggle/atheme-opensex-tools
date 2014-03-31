#! /usr/local/bin/python

from opensex.user import *
from opensex.memo import *
from opensex.channel import *
from opensex.io import *
import codecs, sys

if (len(sys.argv) < 3):
    print "Usage: %s <old.db> <new.db>" % sys.argv[0]
    print "   Output is to STDOUT."
    exit()

# Read in and parse first database
db = open(sys.argv[1], 'r')

for s in db:
    s = s.strip()
    parse(s)

db.close()

# Read in and parse second database
db = open(sys.argv[2], 'r')

for s in db:
    s = s.strip()
    parse(s)

db.close()

#debug()
output()
