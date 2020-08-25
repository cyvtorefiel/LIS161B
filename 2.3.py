nums = []

while True:
    num = input ("Enter number: ")
    if num == "done":
        break

    try:
        num = int(num)
    except:
        print("Bad input")
        continue

    nums.append(num)

if len(nums) == 0:
    print(sum(nums), lens(nums), None, None)
else:
    print(sum(nums), len(nums), max(nums), min(nums))
