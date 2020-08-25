import sys

def every_three_nums(start):
    list = []
    end = 100

    if start > 100:
        return list

    else:
        while True:
            if start <= 100:
                list.append(start)
                start += 3
            else:
                break

        return list


for line in sys.stdin:
    if 'exit' == line.rstrip():
        break
    else:
        start =  int(line)
        print(every_three_nums(start))
        break
