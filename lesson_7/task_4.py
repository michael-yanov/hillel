def season(month):
    m = ''
    if month == 1 or month == 2 or month == 12:
        m = 'Winter'
    elif month == 3 or month == 4 or month == 5:
        m = 'Spring'
    elif month == 6 or month == 7 or month == 8:
        m = 'Summer'
    elif month == 9 or month == 10 or month == 11:
        m = 'Autumn'
    else:
        print('Wrong input')
    return m


print(season(12))