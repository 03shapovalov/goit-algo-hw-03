import datetime

def get_days_from_today(date_of_war):
    date_obj = datetime.datetime.strptime(date_of_war, '%Y-%m-%d')
    today = datetime.datetime.today()
    delta = today - date_obj
    return delta.days
date_of_war = '2022-02-24'
defference = get_days_from_today(date_of_war)
print(defference)