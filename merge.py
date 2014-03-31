#! /usr/local/bin/python

from opensex.user import *
import codecs, sys

if (len(sys.argv) < 2):
    print "Usage: %s <atheme.db>" % sys.argv[0]
    exit()

users = []
db = open(sys.argv[1], 'r')

for s in db:
    s = s.strip()
    record = s.split(' ', 1)
    
    if record[0] == 'MU':
        u = User(record[1])
        users.append(u)

db.close()

for u in users:
    print "%s (%s) created %d" % (u.name, u.email, u.created)
