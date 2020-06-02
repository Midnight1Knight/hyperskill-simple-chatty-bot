min_ = int(input())
max_ = int(input())
slept = int(input())
if min_ <= slept <= max_:
    print("Normal")
elif min_ > slept:
    print("Deficiency")
elif slept > max_:
    print("Excess")
