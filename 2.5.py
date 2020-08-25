fname = input("Enter filename: ")

try:
    fhandle = open(fname)
except:
    print("File not found")
    exit()


days = {}

for line in fhandle:
    if line.startswith('From '):
        day = line.split()[2]
        #if day in days:
        #    days[day] += 1
        #else:
        #    days[day] = 1
        days[day] = days.get(day, 0) + 1

print(days)
