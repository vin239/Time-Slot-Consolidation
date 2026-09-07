n = int(input())

arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])

arr.sort()

ans = []

for a, b in arr:
    if not ans or a > ans[-1][1]:
        ans.append([a, b])
    else:
        ans[-1][1] = max(ans[-1][1], b)

for a, b in ans:
    print(a, b)
