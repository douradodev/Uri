x, y = map(int, input().split())

print(int(((x + y)*len(range(x, y+1)))/2))