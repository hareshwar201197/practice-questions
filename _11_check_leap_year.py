# check given year is leap year or not
year = int(input("Enter the year :"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("is a leap year",year)
        else:
            print("is not a leap year",year)
    else:
        print("is a leap year",year)
else:
    print("Not a leap year ",year)
