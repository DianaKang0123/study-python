class Office:
    def __init__(self,id:str,name:str,location:str,conference_rooms:tuple ):
        self.id = id
        self.name = name
        self.location = location
        self.conference_room = conference_rooms

    def __str__(self):
        room_str = ""
        for conference_room in self.conference_rooms:
            room_str += f'{conference_room.id} 번 회의실\n'

        return room_str