n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse = True)

first_num = data[0]
second_num = data[1]

total = 0

while True:
    for i in range(k):
        if m == 0:
            break
        total += first_num
        m -= 1
    
    if m == 0:
        break
    total += second_num
    m -= 1
    

print(total)