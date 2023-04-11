cnp=input()
def ValidatorCNP(cnp):


    if len(cnp) != 13:
        return False
    sex = cnp[0]
    year = int(cnp[1:3])
    month = int(cnp[3:5])
    day = cnp[5:7]
    county_code = int(cnp[7:9])
    control = int(cnp[12])

    if sex in [1,2]:
        year+=1900

    if sex in [3,4]:
        year+=1800

    if sex in [5,6]:
        year+=2000

    if sex not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return False

    if month not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        return False


    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0:
        days_in_month[1] = 29

    if not int(day) <= days_in_month[int(month) - 1]:
        return False

    if county_code > 52 or county_code==0:
        return False

    nr = int(sex)*2+ int(cnp[1])*7 + int(cnp[2])*9 + int(cnp[3])*1 + int(cnp[4])*4 + int(cnp[5])*6 +int(cnp[6])*3 + int(cnp[7])*5 + int(cnp[8])*8 + int(cnp[9])*2 + int(cnp[10])*7 +  int(cnp[11])*9
    control2 =nr % 11
    if control2 == 10:
        control2=1
    if control != control2:
        return False

    return True