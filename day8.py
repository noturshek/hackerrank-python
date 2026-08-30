if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sets = set(arr)
    print(sorted(sets, reverse=True)[1])
