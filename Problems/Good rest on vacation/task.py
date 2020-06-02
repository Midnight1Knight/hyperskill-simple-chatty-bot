# put your python code here
duration = int(input())
cost_food = int(input())
flight = int(input())
night_in_hotel = int(input())
print(cost_food * duration + night_in_hotel * (duration - 1)
      + flight * 2)
