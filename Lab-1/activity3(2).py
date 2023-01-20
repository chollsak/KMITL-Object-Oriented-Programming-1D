import math

in_hour, in_min, out_hour, out_min = input("Enter entry and exit time in the format 'HH:MM HH:MM': ").split()

total_time = (int(out_hour) - int(in_hour))*60 + (int(out_min) - int(in_min))

if total_time <= 15:
    total_payment = 0
elif 15 < total_time <= 180:
    total_payment = math.ceil(total_time/60)*10
elif 180 < total_time <= 360:
    total_payment = math.ceil(total_time/60)*20 + 10
else:
    total_payment = 200

print(f'Parking fee: {total_payment} THB')
