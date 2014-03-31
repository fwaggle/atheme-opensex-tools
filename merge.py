#! /usr/local/bin/python

from opensex.user import *
import codecs, sys

if (len(sys.argv) < 2):
    print "Usage: %s <atheme.db>" % sys.argv[0]
    exit()

users = {}
db = open(sys.argv[1], 'r')

for s in db:
    s = s.strip()
    record = s.split(' ', 1)
    
    # MD: User record
    if record[0] == 'MU':
        u = User(record[1])
        users[u.name] = u

    # MD: metadata?
    elif record[0] == 'MD':
        type = record[1].split(' ', 1)
        
        # User metadata
        if type[0] == 'U':
            meta = type[1].split(' ', 2)
            if meta[0] in users:
                u = users[meta[0]]
                u.meta[meta[1]] = meta[2]
            else:
                print "Warning: Metadata found for nonexistent user: %s" % meta[0]

    # MN: User nick registration
    elif record[0] == 'MN':
        nick = record[1].split(' ', 1)
        
        if nick[0] in users:
            u = users[nick[0]]
            n = Nick(nick[1])
            u.nicks[n.name] = n
        else:
            print "Warning: Nickname registration for nonexistent user: %s" % nick[0]

db.close()

#exit()

for u in users:
    user = users[u]
    print "%s (%s) created %d" % (user.name, user.email, user.created)
    print ("\tNicknames: "), # fuck python3
    for n in user.nicks:
        print(" %s" % n),
    print ""
    print "\t %s" % user.meta
