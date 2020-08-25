if __name__ == '__main__':

    a = int(input())
    students = []
    for _ in range(a):
        if a >= 2 and a <= 5:
            name = input()
            score = float(input())
            students.append([name, score])

    for i in students:
        print(i)
        for j in i:
            print(j)
    #lowest =
    #students = sorted(students)[1]
    #print(students)
