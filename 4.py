#Write a program to prompt the user for hours and rate per hour to compute gross pay
#also handls non-numeric input

hours = input("Enter hour: ")

try:
    hours = float(hours)
except:
    print("Value Error for hours")
    exit()

rate = input("Enter rate: ")

try:
    rate = float(rate)
except:
    print("Value Error for rate")
    exit()

if hours > 40:
    pay = 40 * rate + (hours - 40) * rate * 1.5
else:
    pay = hours * rate

print("Pay:", pay)
