fname = input("Enter filename: ")

try:
    fhandle = open(fname)
except:
    print("File not found")
    exit()


emails = {}

for line in fhandle:
    if line.startswith('From '):
        email = line.split()[1]
        emails[email] = emails.get(email, 0) + 1

email_count_max = 0
email_max = ''

for email in emails:
#for key,value in emails.items():
    if emails[email] > email_count_max:
    #if value > email_count_max:
        email_count_max = emails[email]
        #email_count_max = v
        email_max = email
        #email_max = k

print(email_max, email_count_max)
