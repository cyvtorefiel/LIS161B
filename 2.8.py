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


emails_list_tup = []

for key,value in emails.items():
    emails_list_tup.append((value, key))

email_count_max, email_max = sorted(emails_list_tup
print(sorted(emails_list_tup))
