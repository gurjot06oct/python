import random
import datetime

def random_date_generator(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date


def random_name_generator():
    syllables = ['ba', 'be', 'bi', 'bo', 'bu', 'da', 'de', 'di', 'do', 'du']
    return ''.join(random.choices(syllables, k=random.randint(2, 3))).capitalize()
