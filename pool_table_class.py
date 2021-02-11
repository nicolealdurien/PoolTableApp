#WEEK 2 DAYS 3-5: POOL TABLE APP

import datetime
import pickle

class PoolTable:
    def __init__(self, table_number):
        self.table_number = table_number
        self.is_occupied = False
        self.start_strptime = None 
        self.start_strftime = None
        self.end_time = None


def occupancy_check():
    for table in table_list:
        if table.is_occupied == True:
            continue
        else:
            print(f"Pool Table #{table.table_number} is available for play.")


def assign_table(table):
    with open("02-10-2021.txt", "a") as table_log:
        if table.is_occupied == True:
            print("STOP - This table is occupied.")
        elif table.is_occupied == False:
            table.is_occupied = True
            table.start_strptime = datetime.datetime.now().strptime
            table.start_strftime = datetime.datetime.now().strftime("%I:%M %p on %m/%d/%Y")
            table_log.write(f"Pool Table #{table.table_number} in use; beginning at {table.start_strftime}\n")  
            print(f"Pool Table #{table.table_number} in use; beginning at {table.start_strftime}")
        

t_one = PoolTable(1)
t_two = PoolTable(2)
t_three = PoolTable(3)
t_four = PoolTable(4)
t_five = PoolTable(5)
t_six = PoolTable(6)
t_seven = PoolTable(7)
t_eight = PoolTable(8)
t_nine = PoolTable(9)
t_ten = PoolTable(10)
t_eleven = PoolTable(11)
t_twelve = PoolTable(12)

start_list = [t_one, t_two, t_three, t_four, t_five, t_six, t_seven, t_eight, t_nine, t_ten, t_eleven, t_twelve]

# #Business Logic

#     def check_out(self):
#         self.is_occupied = False
#         self.end_time = datetime.datetime.now()


#     def get_time_played(self):
#         return self.end_time - self.start_time



