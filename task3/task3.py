M = int(input())
for i in range ((M+1)//2,0,-1):
    if (M % (i**2)) == 0:
        print(i**2)
        break