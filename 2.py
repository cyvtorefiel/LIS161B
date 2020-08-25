hours = input("Enter hour: ")

try:
    hours = float(hours)
except:
    print("Value error for hours")

rate = float(input("Enter rate: "))
try:
    rate = float(rate)
except:
    print("Value error for hours")

if hours > 40:
    pay = 40 * rate + (hours - 40) * rate * 1.5
else:
    pay = hours * rate
