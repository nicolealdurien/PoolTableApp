#WEEK 2 DAYS 3-5: POOL TABLE APP

import datetime

class PoolTable:
    def __init__(self, table_number):
        self.table_number = table_number
        self.is_occupied = False
        self.start_strptime = None 
        self.start_strftime = None
        self.end_time = None


    def occupancy_check(self):
        if self.is_occupied == True:
            print(f"STOP - Pool Table #{self.table_number} is NOT available for play.")
        else:
            print(f"Pool Table #{self.table_number} is available for play.")


    def assign_table(self):
        with open("02-11-2021.txt", "a") as table_log:
            if self.is_occupied == True:
                print("STOP - This table is occupied.")
            elif self.is_occupied == False:
                self.is_occupied = True
                self.start_strptime = datetime.datetime.now().strptime
                self.start_strftime = datetime.datetime.now().strftime("%I:%M %p on %m/%d/%Y")
                table = {"table_number" : self.table_number), "is_occupied": self.is_occupied, "self.start_strftime": self.start_strftime}
                print(table)
                #table_log.write(f"Pool Table #{table.table_number} in use; beginning at {table.start_strftime}\n")  
                # print(f"Pool Table #{table.table_number} in use; beginning at {table.start_strftime}")
        
# def close_out_table(self):


# #Business Logic

#     def check_out(self):
#         self.is_occupied = False
#         self.end_time = datetime.datetime.now()


#     def get_time_played(self):
#         return self.end_time - self.start_time



