fname = input("Enter filename: ")

try:
    fhandle = open(fname)
except:
    print("File not found")
    exit()


bag_of_word = []
for line in fhandle:
    words = line.split()
    for word in words:
        if word not in bag_of_word:
            bag_of_word.append(word)

print(sorted(bag_of_word))    
