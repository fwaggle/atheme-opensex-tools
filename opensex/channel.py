class Channel(object):
    # stole these variable names from jilles' hybservtoatheme.pl
    id = 0
    name = None
    founder = None
    registered = 0
    lastused = 0
    flags = 0
    access = None
    meta = None
    
    def __init__(self, record):
        channel = record.split(' ', 3)
        
        self.name = channel[0]
        self.registered = int(channel[1])
        self.lastused = int(channel[2])
        self.flags = channel[3]
        self.access = {}
        self.meta = {}
