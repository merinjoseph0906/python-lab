print("enter the startyear")
startyear = int(input())
print("enter the lastyear")
lastyear = int(input())
print("list of leap years:")
for year in range(startyear,lastyear):
    if(year % 4 == 0) and (0 != year % 100) or  (year % 400 == 0):
        print(year)