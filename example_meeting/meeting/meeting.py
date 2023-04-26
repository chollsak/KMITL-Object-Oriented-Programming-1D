from datetime import datetime

class MeetingScheduler:
    def __init__(self):
        self.__meeting_room_list = []
        self.__user_list = []

    def add_room(self, room):
        self.__meeting_room_list.append(room)

    def add_user(self, user):
        self.__user_list.append(user)

    def find_available_room(self, start_date, start_time, end_date, end_time, capacity):
        date1 = datetime.strptime(start_date + " " + start_time, '%d-%m-%Y %H:%M')
        date2 = datetime.strptime(end_date + " " + end_time, '%d-%m-%Y %H:%M')
        available_room = []
        for i in self.__meeting_room_list:
            if not i.is_available:
                continue
            if i.capacity < capacity:
                continue
            if not i.room_available(date1, date2):
                continue
            available_room.append(i)
        return available_room

    def list_room(self):
        for i in self.__meeting_room_list:
            print(i)

class User:
    def __init__(self, name):
        self.__name = name

class Interval:
    def __init__(self, start_time, end_time):
        self.__start_time = start_time
        self.__end_time = end_time

class Meeting:
    def __init__(self, subject, meeting_room, interval):
        self.__subject = subject
        self.__meeting_room = meeting_room
        self.__interval = interval

class Calendar:
    def __init__(self):
        self.__meeting_list = []

class MeetingRoom:
    def __init__(self, id, capacity):
        self.__id = id
        self.__capacity = capacity
        self.__is_available = True
        self.__interval_list = []

    def is_available(self):
        return self.__is_available

    @property
    def capacity(self):
        return self.__capacity

    def add_interval(self, interval):
        self.__interval_list.append(interval)

    def check_no_overlap(start_time1, end_time1, start_time2, end_time2):
        if start_time1 > end_time2 or start_time2 > end_time1:
            return True
        else:
            return False

    def room_available(self, datetime1, datetime2):
        for i in self.__interval_list:
            if not self.check_no_overlap(i.get_start_time, i.get_end_time, datetime1, datetime2):
                return False
        return True

    def __str__(self):
        return(f"Room id : {self.__id} capacity {self.__capacity}")



def main():
    meet = MeetingScheduler()
    for i in range(10):
        room_id = i + 1
        room_capacity = (i + 1) * 10
        meet.add_room(MeetingRoom(room_id, room_capacity))

    meet.list_room()
    john = User("john")

    a_room = meet.find_available_room("26-03-2023", "09:00", "26-03-2023", "16:00", 30)
    for i in a_room:
        print(i)

if __name__ == "__main__":
    main()

