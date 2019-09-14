#Python 3.7
import os

add = 0
class Main:
    def __init__(self, *args, **kwargs):
        self.intro = input("Press enter to start")
        if self.intro == "":
            pass
        else:
            Main()
        self.hoursList = []
        self.number_of_days = 0
        self.count_list = 0
        self.hours()

    def hours(self):
        startTime = input("Enter start time: ")
        string_start_time = str(startTime)
        self.number_of_days += 1
        endTime = input("Enter end time: ")
        string_end_time = str(endTime)

        if len(string_start_time) == 3:
            hour_start = int(string_start_time[0])
            minutes_start = int(string_start_time[1:])

            total_minutes_start = ((hour_start * 60) + minutes_start)

        if len(string_end_time) == 3:
            hour_end = int(string_end_time[0])
            minutes_end = int(string_end_time[1:])
            total_minutes_end = ((hour_end * 60) + minutes_end)

        total_time_minutes = total_minutes_end - total_minutes_start

        self.hoursList.append(total_time_minutes)
        print(self.hoursList)
        new = input("type new to enter a new time and done to finalize")
        if new == "new":
            self.hours()
        elif new == "done":
            self.finish()

    def finish(self):
        global add
        try:
            add += self.hoursList[self.count_list]
            self.count_list += 1
            self.finish()
        except:
            os.system("CLS")
            print(str(self.hoursList) + " minutes")
            self.end()
    def end(self):
        print("Total of " + str(len(self.hoursList)) + " entries")
        print(str(add) + " total minutes")
        print(str(add / 60) + " total hours")
        a = input("press any key to close")
        if a == a:
            return 0


Main()
