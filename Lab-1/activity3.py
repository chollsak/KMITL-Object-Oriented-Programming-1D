import math
in_hour, in_min, out_hour, out_min = input("").split()

total_hour = int(out_hour) - int(in_hour)
total_min = int(out_min) - int(in_min)

total_payment = 0
total_time = (total_hour*60) + total_min

if total_time <= 15:
    total_payment = 0

elif total_time > 15 and total_time <= 180:
    total_payment = math.ceil(total_time / 60) * 10

elif total_time > 180 and total_time  <= 360:
    total_payment =  ((math.ceil((total_time - 180) / 60)) * 20) + 30

elif total_time > 360:
    total_payment = 200


print(total_payment)