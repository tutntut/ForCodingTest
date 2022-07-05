n, m = map(int, input().split())
lst = []
for i in range(n):
    lst.append(map(int,input().split()))

lst2 = []

for i in range(n):
    lst2.append(min(lst[i]))

answer = max(lst2)

print(answer)