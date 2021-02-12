#WEEK 2 DAYS 3-5: POOL TABLE APP
#It works and writes to json, recognized by json.lint as valid. Whether it's capturing
# the correct info, and whether I can read back out of it, is to be determined tomorrow.

import json
import datetime
now = datetime.datetime.now()
today = now.date()
tables = []

class PoolTable:
    def __init__(self, ident):
        self.ident = ident
        self.is_occupied = False
        self.start_time = datetime.datetime.now()
        self.end_time = datetime.datetime.now()

    
    def check_out_to_players(self):
        start_timestamp = format_time(datetime.datetime.now())
        self.start_time = datetime.datetime.now()
        self.is_occupied = True
        print("\n- - - - - - - - - - - - - - -")
        print(f"\nPlay started at Table #{str(self.ident)} on {start_timestamp}")


    def return_from_use(self):
        end_timestamp = format_time(datetime.datetime.now())
        self.end_time = datetime.datetime.now()
        self.is_occupied = False
        print("\n- - - - - - - - - - - - - - -")
        print(f"\nPlay ended at Table #{str(self.ident)} on {end_timestamp}")
        

    def total_time_played(self):
        delta = self.end_time - self.start_time
        seconds = delta.seconds
        hours = seconds // 3600
        remaining_secs = seconds - (hours * 3600)
        minutes = remaining_secs // 60
        print('\nTotal Time Played: {:02} hours, {:02} minutes'.format(int(hours), int(minutes)))


# MAKE TIME PRETTY
def format_time(time):
    timestamp = time.strftime("%m/%d/%y at %I:%M %p")
    str_timestamp = timestamp
    return str_timestamp



#OCCUPANCY CHECK
def occupancy_check():
    print("\n- - - - - Table List - - - - -\n")
    for table in tables:
        if table.is_occupied == True:
            print(f"Table #{table.ident} - OCCUPIED")
        else:
            print(f"Table #{table.ident} - VACANT")
    print("\n")

# GIVE EMPTY TABLE TO PLAYERS
def assign_table():
    occupancy_check()
    pick = int(input("Please select a vacant table to assign: "))
    chosen = tables[pick-1]
    if chosen.is_occupied == True:
        print("\nSTOP - This table is already occupied. Please select a vacant table from the list.")
    else:
        chosen.check_out_to_players()
    morph_for_json(tables)
    

# RETURN IN-USE TABLE BACK TO EMPTY WHEN PLAYERS ARE DONE
def close_out_table():
    occupancy_check()
    pick = int(input("Please select an occupied table to close out: "))
    chosen = tables[pick-1]
    chosen.return_from_use()
    morph_for_json(tables)
    chosen.total_time_played()


# Morph List of Table Objects to List of Dictionaries with Object Values, for Writing To a File:
def morph_for_json(list):
    dictionary_list = []
    for table in tables:
        int_ident = int(table.ident)
        bool_occupancy = bool(table.is_occupied)
        str_start = str(table.start_time)
        str_end = str(table.end_time)  
        table_dict = {
            "ident": int_ident, 
            "is_occupied": bool_occupancy, 
            "start_time": str_start, 
            "end_time": str_end
            }
        dictionary_list.append(table_dict)
    with open (f"{today}.json", "w") as file_object:
        json.dump(dictionary_list, file_object)


# Creation of List of Table Objects, List of Dictionaries with Object Values, Initial Write to File
for index in range(12):
    table = PoolTable(index+1)
    tables.append(table)
    morph_for_json(tables)


# MENU ESTA AQUI
while True:
    print("\n- - - - - POOL HALL OVERSIGHT MENU - - - - -")
    choice = input("Press 1 to assign a table.\nPress 2 to close out a table.\nPress q to quit.\n\nYour selection: ")
    if choice == "1":
        assign_table()
    if choice == "2":
        close_out_table()
    if choice == "q":
        break
    else:
        print("\nPlease select an option from the menu: ")