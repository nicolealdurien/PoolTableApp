#WEEK 2 DAYS 3-5: POOL TABLE APP
#It works and writes to json, recognized by json.lint as valid. Whether it's capturing
# the correct info, and whether I can read back out of it, is to be determined tomorrow.

import json
import datetime
tables = []
dictionaries = []

class PoolTable:
    def __init__(self, ident):
        self.ident = ident
        self.is_occupied = False
        self.start_time = datetime.datetime.now()
        self.end_time = datetime.datetime.now()

    
    def check_out_to_players(self):
        string_start = datetime.datetime.now().strftime("%m/%d/%y at %I:%M %p")
        self.start_time = string_start
        self.is_occupied = True
        print("\n- - - - - - - - - - - - - - -")
        print(f"\nPlay started at Table #{str(self.ident)} at {self.start_time}")


    def return_from_use(self):
        string_end = datetime.datetime.now().strftime("%m/%d/%y at %I:%M %p")
        self.end_time = string_end
        self.is_occupied = False
        print("\n- - - - - - - - - - - - - - -")
        print(f"\nPlay ended on Table #{str(self.ident)} at {self.end_time}")
        

    def total_time_played(self):
        delta = self.end_time - self.start_time
        seconds = delta.seconds
        hours = seconds // 3600
        remaining_secs = seconds - (hours * 3600)
        minutes = remaining_secs // 60
        print('\nTotal Time Played: {:02} hours, {:02} minutes'.format(int(hours), int(minutes)))


# GIVE EMPTY TABLE TO PLAYERS
def assign_table():
    print("\n- - - - - Vacant Tables - - - - -")
    for table in tables:
        if table.is_occupied == False:
            print(f"Table #{table.ident}")
    pick = int(input("Please select a table: "))
    chosen = tables[pick-1]
    if chosen.is_occupied == True:
        print("\nSTOP - This table is already occupied. Please select a vacant table from the list.")
    else:
        chosen.check_out_to_players()
    int_ident = int(chosen.ident)
    bool_occupancy = bool(chosen.is_occupied)
    str_start = str(chosen.start_time)
    str_end = str(chosen.end_time)  
    chosen_dict = {"ident": int_ident, "is_occupied": bool_occupancy, "start_time": str_start, "end_time": str_end}
    dictionaries[pick-1] = chosen_dict
    print(dictionaries[pick-1])
    with open("02-11-2021.json", "w") as table_log:
        json.dump(dictionaries, table_log)

    


# RETURN IN-USE TABLE BACK TO EMPTY WHEN PLAYERS ARE DONE
def close_out_table():
    print("\n- - - - - Currently Occupied Tables - - - - -")
    for table in tables:
        if table.is_occupied == True:
            print("Table #" + str(table.ident) + " - Play started at " + table.start_time.strftime("%H:%M"))
    pick = int(input("Please select a table to close out: "))
    chosen = tables[pick-1]
    chosen.return_from_use()
    int_ident = int(chosen.ident)
    bool_occupancy = bool(chosen.is_occupied)
    str_start = str(chosen.start_time)
    str_end = str(chosen.end_time)  
    chosen_dict = {"ident": int_ident, "is_occupied": bool_occupancy, "start_time": str_start, "end_time": str_end}
    dictionaries[pick-1] = chosen_dict
    with open("02-11-2021.json", "w") as table_log:
       json.dump(dictionaries, table_log)
    chosen.total_time_played()


# Morph List of Table Objects to List of Dictionaries with Object Values, for Writing To a File:
def morph_for_json():
    for table in tables:
        int_ident = int(table.ident)
        bool_occupancy = bool(table.is_occupied)
        str_start = str(table.start_time)
        str_end = str(table.end_time)  
        table_dict = {"ident": int_ident, "is_occupied": bool_occupancy, "start_time": str_start, "end_time": str_end}
        dictionaries.append(table_dict)


# Creation of List of Table Objects, List of Dictionaries with Object Values, Initial Write to File
for index in range(12):
    table = PoolTable(index+1)
    tables.append(table)
    morph_for_json()

# MENU ESTA AQUI
while True:
    print("\n- - - - - POOL HALL OVERSIGHT MENU - - - - -")
    choice = input("Press 1 to assign a table.\nPress 2 to close out a table.\nPress q to quit.\nYour selection: ")
    if choice == "1":
        assign_table()
    if choice == "2":
        close_out_table()
    if choice == "q":
        break