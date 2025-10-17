#question 1
# getttingb natural numbers and storing them in a list
k=int(input("entr number"))
l=[]
c=0
while c <k:
    c+=1
    (l.append(c))
print(l)
# using break in loop
k=int(input("enter number"))
i=0
while i <100:
    if i ==50:
        break
    i+=2
    print(i)
# continue statement
k=int(input("enter number"))
i=0
while i < k:
    if i==6:
        continue
    i+=2
    print(i)
# print al the even number that falls between two number taken from user
num1=int(input("enter number1:  "))
num2=int(input("enter number2:  "))
if num1>num2 and (num1 and num2)%2==0:
    while num2<num1:
        print(num2)
        num2+=2
elif num2>num1 and (num1 and num2)%2==0:
    while num1 <num2:
        print(num1)
        num1+=2
# wap to find the sum of the number enterd by the input
num1=int(input("enter number: "))
s=0
r=0
while num1!=0:
    r=num1%10
    s+=r
    num1=num1//10
print(s)
# wap to get the product of the number given byy the user
num1=int(input("enter number: "))
s=1
r=0
while num1!=0:
    r=num1%10
    s*=r
    num1=num1//10
print(s)
# WAP  to take integer input from the usser and print it the the name of the numberr
num1=input('entr number')
L=list(num1)
l1=len(L)
n={0: "zero" , 1: "one" , 2: "two", 3: "three" , 4: "four" , 5: "five" , 6: "six" , 7: "seven" , 8: "eight", 9: "ninne"}
i=0
while i < l1:
    print(n[int(L[i])] , end=" ")
    i+=1
#WAP to check if a number is palindrome or not
n=int(input("enter number"))
temp=n
rev=0
while n> 0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
if temp==rev:
    print('number is palindrrome')
else:
    print('number is not palindrome')
# wap to take ten integer input from the user and prinr the maximum and minimum number
L=[]
i=0
while i <10:
    x=int(input("enter number:  "))
    i+=1
    L.append(x)
print(L)
print( "maximum number is: ", max(L))
print("minimum number is: ",min(L))
# wap to find the factorial of any number
um=int(input("enter any number"))
if num==0:
    print(1)

else:
    fact=1
    while num>0:
        fact=fact*num
        num-=1
print(fact)


#question 2
odd_number=[]
even_number=[]
while True:
    user_input=input("enter number:  ")
    if user_input=="x":
        break
    num=int(user_input)
    if num%2==0:
        even_number.append(num)
    else:
        odd_number.append(num)
print(even_number)
ab=sum(even_number)
c=len(even_number)
print("average of even number is :" , (ab)/c)
print(odd_number)
ba=sum(odd_number)
d=len(odd_number)
print("average of odd_number:" , (ba)/d)
# question 3
n=int(input("enter number:  "))
numbers=" "
total_number=0
for i in range(1,n+1):
    numbers+=str(i)
    num=int(numbers)
    total_number+=num
print(total_number)
# question 4
for i in range(200,2000):
    digit=str(i)
    power=len(digit)
    
    output=sum(int(d)**power  for d in digit)
    if output== i:
        print(i,"is a amstrong number")
# question 5
lst=[]
user_input=input("enter anything:  ")
while True:
    if user_input=="x":
        break
    else:
        lst.append(user_input)
        print(user_input)
# question5
lst=[]
while True:
    user_input=input("enter anything:  ")
    if user_input=="x":
        break
    cd=str(user_input)
    lst.append(cd)
print(lst)
for elements in lst:
    rev=elements[::-1]
    if rev==elements:
        print(elements,"palindrome")
    else:
        print(elements,"not palindrome")
