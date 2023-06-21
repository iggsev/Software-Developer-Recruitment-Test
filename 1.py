from datetime import datetime, timedelta


def get_weekdays_between_dates(start_date, end_date):
    weekdays = []

    while start_date <= end_date:
        if start_date.weekday() < 5:
            weekdays.append(start_date.strftime('%Y-%m-%d'))

        start_date += timedelta(days=1)

    return weekdays

def weekdays_until_end_of_next_month(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')

    last_day_of_current_month = datetime(date.year, date.month, 1) + timedelta(days=32)
    end_of_current_month = last_day_of_current_month.replace(day=1) - timedelta(days=1)

    if date.month == 12:
        end_of_next_month = datetime(date.year + 1, 1, 1)
    else:
        end_of_next_month = datetime(date.year, date.month + 2, 1) - timedelta(days=1)
    
    weekdays = get_weekdays_between_dates(date, end_of_current_month)

    weekdays += get_weekdays_between_dates(end_of_current_month + timedelta(days=1), end_of_next_month)

    return weekdays


print( weekdays_until_end_of_next_month('2023-03-26')) 
