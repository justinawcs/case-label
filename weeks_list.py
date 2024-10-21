import datetime
import case_label

# def week_letter(iso_date_string=None):
#     d = datetime.datetime.now().strftime("%V")
#     if iso_date_string is not None:
#         d = datetime.date.fromisoformat(iso_date_string).strftime("%V")
#     alpha = list(string.ascii_uppercase)
#     #alpha = list("ZA").append(alpha)
#     index = int(d) % 26
#     result = alpha[index-1]
#     if int(d) == 53:
#         result = "ZA"
#     return "Week #{}: {}".format(d, result)

def make_list(year=None):
    result = ""
    result += "Weeks are in ISO-8601 format.\nFor details visit: https://www.epochconverter.com/weeks\n\n"
    date = datetime.date.fromisoformat("2000-12-24").replace(year=datetime.date.today().year - 1)
    if year is not None:
        date = datetime.date.fromisoformat("2000-12-24").replace(year=year)
    date = date - datetime.timedelta(days=date.weekday())  # move day to Monday
    wk = datetime.timedelta(days=7)
    for i in range(56):
        result += str(date) + " Starts " + case_label.week_letter(str(date)) +"\n"
        date += wk
    return result

def main():
    print(make_list())

if __name__ == '__main__':
    main()