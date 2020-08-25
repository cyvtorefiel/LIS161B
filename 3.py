#Write a program to prompt the user for hours and rate per hour to compute gross pay

hours = float(input("Enter hour: "))
rate = float(input("Enter rate: "))

if hours > 40:
    pay = 40 * rate + (hours - 40) * rate * 1.5
else:
    pay = hours * rate

print("Pay:", pay)
