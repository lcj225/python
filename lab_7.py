a = 0
b = 0
while a < 1000:
    a += 1
    if a % 3 == 0:
        b = b+a

print(b)

a = 0
b = '*'
while a < 5:
    print(b)
    b = b+'*'
    a += 1

for i in range(0,101):
    print(i)

a = [70,60,55,75,95,90,80,80,85,100]
b = 0
for i in a:
    b = b+i
print(round(b/10,len(a)))

numbers = [1,2,3,4,5]
result = [i*2 for i in numbers if i%2 == 1]
print(result)