import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

date = datetime.datetime(2020, 12, 24)
print(date.strftime("%d"))
print(date.strftime("%m"))


def has_friday_13(month, year):
    import datetime
    y = datetime.datetime(year, month, 13)
    if y.strftime("%A") == "Friday":
        return True
    else:
        return False


def time_for_milk_and_cookies(date):
    print(type(date.strftime("%d")))
    if date.strftime("%d") == "24" and date.strftime("%m") == "12":
        return True
    else:
        return False


print(time_for_milk_and_cookies(datetime.date(2013, 12, 24)))

