_ = int(input())

for i in range(_):
    a,b,r = map(int,input().split())
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    for i in arr:
        if a + b > i:
            if a + i > b:
                if b + i > a:
                    count = count + 1
    
    print(count)
    if count > r:
        print("Natsu")
    else:
        print("Grey")
