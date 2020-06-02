# put your python code here
def are_leap(year):
    if (year % 400 == 0) or ((year % 4 == 0) and not (year % 100 == 0)):
        return True
    return False


year_ = int(input())
if are_leap(year_):
    print("Leap")
else:
    print("Ordinary")
