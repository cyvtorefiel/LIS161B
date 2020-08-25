if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    print(max([i for i in arr if i != max(arr)]))
