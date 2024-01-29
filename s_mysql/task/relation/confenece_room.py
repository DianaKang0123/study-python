
class ConfenceRoom:
    def __init__(self,id:str,part_times: tuple):
        self.id = id
        self.part_times = part_times

    def __str__(self):
        time_str = ""
        for time in self.part_times:
            time_str += time + "\n"

        return time_str