from datetime import datetime

def get_birthdays_per_week(users):
    today = datetime.today().date()
    greet_dict = {}
    # today_weekday = today.weekday()
    # start_weekday = 5 - today_weekday
    # end_weekday = 11 - today_weekday
    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        birthday_this_year = birthday.replace(year=today.year)
        
        difference_days = birthday_this_year - today
        difference_days = difference_days.days
        # print(birthday_this_year.strftime('%A'), name)
        
        if (difference_days >= 1 and 
            difference_days <= 7):
            birthday_weekday = birthday_this_year.strftime('%A')
            if birthday_weekday in ['Saturday', 'Sunday']:
                birthday_weekday = 'Monday'
            try:
                greet_dict[birthday_weekday].append(name)
            except:
                greet_dict[birthday_weekday] = [name]
        # print(difference_days)
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
                'Friday', 'Saturday', 'Sunday']
    for weekday in weekdays:
        try:
            birthday_names = ', '.join(greet_dict[weekday])
            # print(names)
            print(f'{weekday}: {birthday_names}')
        except:
            continue

if __name__ == "__main__":
    users = [
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 12)},      
        {"name": "Bob Tom", "birthday": datetime(1935, 10, 18)}
            ]
    get_birthdays_per_week(users)

