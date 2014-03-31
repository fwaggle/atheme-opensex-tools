class User(object):
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
        r = record.split(' ', 5)
        
        self.name = r[0]
        self.password = r[1]
        self.email = r[2]
        self.created = int(r[3])
        self.seen = int(r[4])
        self.flags = r[5]
        self.meta = {}
        self.nicks = {}

class Nick(object):
    name = None
    created = 0
    seen = 0
    
    def __init__(self, record):
        r = record.split(' ')
        
        self.name = r[0]
        self.created = r[1]
        self.seen = r[2]