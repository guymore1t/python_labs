min1 = int(input())

hours = min1 // 60
min2 = min1 % 60

if min1 % 60 != 0:
    print(hours,':',min2,sep = '')

else:
    print(hours,':',min2,'0',sep = '')
    

