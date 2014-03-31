lastid = 1

class User(object):
    id = None
    name = None
    password = None
    email = None
    created = 0
    seen = 0
    flags = '0 0 0 0'
    meta = None
    nicks = None
    
    # create empty user
    def __init__(self):
        self.meta = {}
        self.nicks = {}
        pass
    
    # create user from db record
    def __init__(self, record):
        global lastid
        r = record.split(' ', 6)
        
        self.id = lastid
        lastid = int(lastid + 1)
        
        self.name = r[1]
        self.password = r[2]
        self.email = r[3]
        self.created = int(r[4])
        self.seen = int(r[5])
        self.flags = r[6]
        self.meta = {}
        self.nicks = {}

class Nick(object):
    name = None
    created = 0
    seen = 0
    
    def __init__(self, record):
        r = record.split(' ')
        
        self.name = r[0]
        self.created = int(r[1])
        self.seen = int(r[2])
