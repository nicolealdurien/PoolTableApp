from datetime import datetime

def to_datetime_object(date_string, date_format):
    s = datetime.strptime(date_string, date_format)
    return s

time_1 = '2015-08-10 19:33:27'
time_2 = '2015-08-10 19:31:28'
date_format = "%Y-%m-%d %H:%M:%S"
time_1_datetime_object = to_datetime_object(time_1, date_format)
time_2_datetime_object = to_datetime_object(time_2, date_format)

diff_time = time_1_datetime_object - time_2_datetime_object
print(diff_time)