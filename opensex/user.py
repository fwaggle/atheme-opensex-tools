class User:
    name = None
    password = None
    email = None
    created = 0
    seen = 0
    flags = '0 0 0 0'
    
    # create empty user
    def __init__(self):
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
