import datetime

class wamsg:
    def __init__(self, date, time, sender, message=None, filename=None):
        self.date = date
        self.time = time
        # self.dt = datetime.datetime()
        # self.dt.year = 
        # self.dt.month = 
        # self.dt.day = 
        # self.dt.hour = XXX
        # self.dt.minute = XXX
        # self.dt.second = XXX
        self.sender = sender
        self.message = message
        self.filename = None