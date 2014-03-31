class Memo(object):
    ts = 0
    to = None
    sender = None
    flag = 0
    data = None
    
    def __init__(self, record):
        memo = record.split(' ', 4)
        
        self.ts = int(memo[2])
        self.to = memo[0]
        self.sender = memo[1]
        self.flag = int(memo[3])
        self.data = memo[4]
