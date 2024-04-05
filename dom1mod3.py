import datetime

def get_days_from_today(date_of_war):
    try:
        date_obj = datetime.datetime.strptime(date_of_war, '%Y-%m-%d')
        today = datetime.datetime.today()
        delta = today - date_obj
        return delta.days
    except ValueError:
        return "Невірний формат дати, використовуйте формат 'рік-місяць-день', наприклад, '2022-02-24'."
date_of_war = '2022-02-24'
defference = get_days_from_today(date_of_war)
print(f"Від початку вторгнення расії в Україну пройшло днів {defference}")

