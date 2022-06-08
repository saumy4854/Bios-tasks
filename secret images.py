
a = list(map(str, input().split()))
png, bmp, jpeg = 0,0,0
for i in a:
    if ".png" in i:
        png+=1
    elif ".bmp" in i:
        bmp+=1
    elif ".jpeg" in i:
        jpeg+=1
print(png ,bmp, jpeg)