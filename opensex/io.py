from opensex.user import *
from opensex.memo import *
from opensex.channel import *

users = {}
memos = []
channels = []
dbv = None
cf = None
mdep = []

channels_ignore = []

# Parse OpenSEX database
# Note that because this was written for merge.py, it will clobber
# new records with old (by ts). This may not be what you want.
def parse(s):
    global dbv, cf, users, channels, memos
    record = s.split(' ', 1)

    # DBV: Database version - we don't do anything with this    
    if record[0] == 'DBV':
        dbv = record[1]

    # CF: we don't do anything with this either
    elif record[0] == 'CF':
        cf = record[1]

    # MDEP: Module dependencies, we don't touch these
    elif record[0] == 'MDEP':
        mdep.append(record[1])

    # MD: User record
    elif record[0] == 'MU':
        u = User(record[1])
        users[u.name] = u

    # MDU: User Metadata
    elif record[0] == 'MDU':
        meta = record[1].split(' ', 2)
        if meta[0] in users:
            u = users[meta[0]]
            u.meta[meta[1]] = meta[2]
        else:
            print "Warning: Metadata found for nonexistent user: %s" % meta[0]

    # MDC: Channel metadata
    elif record[0] == 'MDC':
        meta = record[1].split(' ', 2)
        chan = None
        
        for c in channels:
            if c.name == meta[0]:
                chan = c
                break
        
        if chan == None:
            print "Warning: Channel metadata record for unknown channel %s" % meta[0]
        else:
            chan.meta[meta[1]] = meta[2]

    # MN: User nick registration
    elif record[0] == 'MN':
        nick = record[1].split(' ', 1)
        
        if nick[0] in users:
            u = users[nick[0]]
            n = Nick(nick[1])
            u.nicks[n.name] = n
        else:
            print "Warning: Nickname registration for nonexistent user: %s" % nick[0]

    # ME: Memos?
    elif record[0] == 'ME':
        memo = Memo(record[1])
        memos.append(memo)

    # MC: Channel record
    elif record[0] == 'MC':
        chan = Channel(record[1])
        
        for c in channels:
            if c.name == chan.name:
                if c.registered <= chan.registered:
#                    print "%s (%d) is older than current, ignoring..." % (chan.name, chan.registered)
                    chan = None
                    channels_ignore.append(c.name)
                    break
                else:
#                    print "Replacing %s (%d) with %s (%d)" % (c.name, c.registered, chan.name, chan.registered)
                    # This channel is newer, blow away the old one
                    channels.remove(c)

        if chan != None:
            channels.append(chan)
    
    # CA: Channel access?
    elif record[0] == 'CA':
        access = record[1].split(' ', 2)
        chan = None
        
        for c in channels:
            if c.name == access[0]:
                chan = c
                break
        
        if chan == None:
            print "Warning: Channel access record for unknown channel %s" % access[0]
        else:
            chan.access[access[1]] = access[2]

#    else:
#        print "Unhandled record type: %s" % record[0]

def output():
    global users, channels, mdep, cf, dbv, memos
    
    print "DBV %d" % int(dbv)
    
    for mod in mdep:
        print "MDEP %s" % mod
    
    # print lastuid
    
    print "CF %s" % cf
    
    # user accounts
    for i in users:
        u = users[i]
        
        print "MU %s %s %s %s %d %d %s" % (encodeid(u.id), u.name, u.password, u.email, u.created, u.seen, u.flags)
        
        # user metadata
        
        for m in u.meta:
            print "MDU %s %s %s" % (u.name, m, u.meta[m])
        
        # user nicks
        for j in u.nicks:
            n = u.nicks[j]
            
            print "MN %s %s %d %d" % (u.name, n.name, n.created, n.seen)
        
    # channels
    for c in channels:
        print "MC %s %d %d %s  " % (c.name, c.registered, c.lastused, c.flags)
        
        # channel access
        for a in c.access:
            print "CA %s %s %s " % (c.name, a, c.access[a])
        
        # channel metadata
        for m in c.meta:
            print "MDC %s %s %s" % (c.name, m, c.meta[m])

# Dump the user and channel objects in memory to stdout        
def debug():
    global users, channels, mdep
    for u in users:
        user = users[u]
        print "%s (%s) created %d" % (user.name, user.email, user.created)
        print ("\tNicknames: "), # fuck python3
        for n in user.nicks:
            print(" %s" % n),
        print ""
        print "\t%s" % user.meta

    for c in channels:
        print "%s registered %d by %s" % (c.name, c.registered, c.founder)
        print "\t%s" % c.meta
        print "  Access list:"
        print "\t%s" % c.access

#    print mdep

def encodeid(input):
    # base 36 on crack or something?
    digits = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890'
    output = ''
    while input:
        input, remainder = divmod(input, 36)
        output = digits[remainder] + output

    return output.rjust(9,'A')
