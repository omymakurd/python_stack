#print all integer from 0 to 150
for x in range(0,150):
  print(x)

#print all the multiples of 5 from 5 to 1000

for x in range(5,1001):
    if x%5 ==0:
      print(x)
#print integers 1 to 100 if divisble by 5 print coding divisble by 10 print coding dojo

for x in range(1,101):
    if  x%10 == 0:
        print( x ,"Coding dojo") 
    elif x%5 == 0:
        print( x ,"Coding")
    else:
        print(x)
#add odd integers from 0 to 500000 and print final sum
sum =0 
for x in range (0,500000):
    if x%2 != 0 :
        sum+=x
print(sum)

#print positive numbers startion at 2018 counting down by fours
for x in range (2018,0,-4):
    print(x)

#Flexible counter
LowNum=2
highNum=9
mult=3
for x in range(LowNum,highNum+1):
    if x%mult == 0:
        print(x)
