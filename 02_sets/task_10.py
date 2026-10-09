lst = list(map(int, input().split()))
target = int(input())

seen = set()
for num in lst:
    complement = target - num
    if complement in seen:
        print(True)
        break
    seen.add(num)
else:   
    print(False)
