#WEEK 2 POOL TABLE PROJECT
#OBJECT CREATION AND USER INPUT CODE GOES HERE 

from pool_table_class import PoolTable


pool_tables = []

for index in range(13):
    pool_table = PoolTable(index+1)
    pool_tables.append(pool_table)



pt_one = pool_tables[0]
pt_one.assign_table()