len=int(input(('1- first Enter the size of your Array :\n\t==> ')))
Sort = []
print('2- Now Enter your number : \n')
for i in range(0,len) :
    print('Number ' , i+1 , ' : ' , end='')
    value = int(input())
    Sort.append(value)

print(Sort)

i = 0
j = 1
c = 1
while j<len :
    if Sort[i]<Sort[j] :
        c +=1
    i +=1
    j +=1

check = 'Yes' if (c == len) else 'NO'
print(check)
