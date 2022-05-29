a = int( input('english:'))
print(a)
b = int(input('tamil:' ))
print(b)
c = int(input('science'))
print (c)
d = int(input('maths'))
print (d)
e = int(input('social'))
print (e)
total = (a+b+c+d+e)
average = (total/5)
if(a>=35 and b>=35 and c>=35 and d>=35 and e>=35):
    print(total)
    if(average<=60):
        print('b grade')
    elif(average<=70):
        print('a grade')
    elif(average>70):
        print('o grade')
   
else:
    print('fail')


