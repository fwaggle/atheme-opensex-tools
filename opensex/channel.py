class Channel(object):
    # stole these variable names from jilles' hybservtoatheme.pl
    name = None
    founder = None
    registered = 0
    lastused = 0
    flags = 0
    lockedon = 0
    lockedoff = 0
    lockedlimit = 0
    access = None
    meta = None
    
    def __init__(self, record):
        channel = record.split(' ', 9)
        
        self.name = channel[0]
        self.founder = channel[2]
        self.registered = int(channel[3])
        self.lastused = int(channel[4])
        self.flags = channel[5]
        self.lockedon = channel[6]
        self.lockedoff = channel[7]
        self.lockedlimit = channel[8]
        self.access = {}
        self.meta = {}
