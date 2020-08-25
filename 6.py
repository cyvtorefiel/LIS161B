fname = input("Enter filename: ")

try:
    fhandle = open(fname)
except:
    print("File not found")
    exit()

dspam_sum = 0
dspam_count = 0

for line in fhandle:
    if line.startswith('X-DSPAM-Confidence:'):
        dspam = float(line[line.find(':')+1:])
        dspam_sum += dspam
        dspam_count += 1

print("Average D-SPAM: ", dspam_sum/dspam_count)
