s=[1,1,1]
s[0] = int(input())
s[1] = int(input())
s[2] = int(input())
x = int(max (s))
y = int(min (s))
m = 0
for i in range(3):
    if int(s[i]) < x and int(s[i]) > y:
        m = s[i]
print(m)