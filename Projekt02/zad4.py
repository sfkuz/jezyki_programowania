def dates_sort(date1, date2):
    if date1["year"] < date2["year"]:
        return True
    elif date1["year"] > date2["year"]:
        return False
    else:
        if date1["month"] < date2["month"]:
            return True
        elif date1["month"] > date2["month"]:
            return False
        else:
            if date1["day"] < date2["day"]:
                return True
            else:
                return False

def sort(dates):
    n = len(dates)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if not dates_sort(dates[j], dates[j+1]):
                dates[j], dates[j+1] = dates[j+1], dates[j]
                swapped = True
        if not swapped:
            break

n = int(input('Podaj liczbę dat: '))
dates = []

for _ in range(n):
    day = int(input('Wprowadź dzień: '))
    month = int(input('Wprowadź miesiąc: '))
    year = int(input('Wprowadź rok: '))
    date = {"day": day, "month": month, "year": year}
    dates.append(date)

sort(dates)
print('Posortowane date')
for date in dates:
    print(f"{date['day']:02d}.{date['month']:02d}.{date['year']}")