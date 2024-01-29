import datetime
class PartTime:
    def __init__(self,id:str,time:datetime.timedelta):
        self.id = id
        self.time = time

    def __str__(self):
        str(self.time)