n = int(input())

arr = []

for i in range(n):
    start, end = map(int, input().split())
    arr.append([start, end])

arr.sort()

result = []

for start, end in arr:
    if len(result) == 0 or start > result[-1][1]:
        result.append([start, end])
    else:
        if end > result[-1][1]:
            result[-1][1] = end

for start, end in result:
    print(start, end)
