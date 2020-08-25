if __name__ == '__main__':
    N = int(input())

    list = []

    for i in range(N):
        cmd = input()

        if cmd.startswith('insert '):
            i = int(cmd.split()[1])
            e = int(cmd.split()[2])
            list.insert(i, e)

        elif cmd.startswith('print'):
            print(list)

        elif cmd.startswith('remove '):
            e = int(cmd.split()[1])
            list.remove(e)

        elif cmd.startswith('append '):
            e = int(cmd.split()[1])
            list.append(e)

        elif cmd.startswith('sort'):
            list = sorted(list)

        elif cmd.startswith('pop'):
            list.pop()

        elif cmd.startswith('reverse'):
            list.reverse()
