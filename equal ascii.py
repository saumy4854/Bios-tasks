# equal ascii ques bios
n = input()
m = input()
sum1 = 0
sum2 = 0
for i in range (len(n)) :
    sum1+=ord(n[i])
for i in range(len(m)):
    sum2+=ord(m[i])
if sum1==sum2:
    print("Equal")
else:
    print("Not equal")