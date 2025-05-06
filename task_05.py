import datetime


def date_in_future(integer):
    if not integer:
        return datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    return (datetime.datetime.now() + datetime.timedelta(integer)).strftime('%d-%m-%Y %H:%M:%S')


print(date_in_future([]))  # => текущая дата
print(date_in_future(2))  # => текущая дата + 2 дня