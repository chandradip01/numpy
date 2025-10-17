#  import random
#  friends=["aadi" , "diksha" , "nandini" , "chandradip"]
#  random1=random.randint(1,5)
#  if random1 == 2:
#      print(friends[0])
# elif random1==4:
#      print(friends[3])
# elif random1 == 1:
#      print(friends[2])
# else:
#      print(friends[1])
# print("hello" + " " + input("what is your name'"))
# print(len(input("what is your name")))
# print("welcome to brand name generator")
# city=input("which city did you belong")
# pet=input("what is the name of pet")
# print(f"your brand name is: {city}{pet}")
# print(int("12345") + int("45678"))
# bmi=84/1.897
# print(int(bmi))
# print(round(bmi , 2))
# "'
#   using astering we can concatinate 
#   string and int "'"
#   ""
#pizza order bill generator
# print("welcome to dominos")
# size=input("type L for large , S for small , M for medium")
# peproni=input("type y for yes and n for no")
# extra_cheese=input("y for yes and no for no")
# bill=0
# if size=="S":
#     bill+=2
# elif size=="M" :
#     bill+=3
# elif size=="L" :
#     bill+=4
# else:
#     print("wrong typing")
# if peproni =="y":
#     if size=="S":
#         bill+=1
# elif peproni == "y":
#     if size=="M" or size=="L":
#         bill+=4
# if extra_cheese=="y":
#     bill+=6
# print(f"your bill is :${bill}")




#logical operators


#treasurhunt  operator
# print("welcome to finding your love game")
# first_choice=input("which icecream she likes choclate or fruit type C for choclate and f for fruit")
# if first_choice=="f":
#     print("you lost")
# else:
#     print("yeah you know her now next level ")
#     second_choice=input("which flower she likes rose or sunflower type R for S")
#     if second_choice=="S":
#         print("you lost")
#     else:
#         print("yeah you knw her pretty well")
#         third_choice=input("you if are in a situtaion where you have to choose her or 100billion doller H for her M for money")
#         if third_choice=="M":
#             print("you lost you are greedy")
#         else:
#             print("congrats you love is real")
#randomisation
# import random
# # random_import=random.randint(1,99)
# # print(random_import )
# random_float=random.uniform(1,10)
# print(random_float)

# fruits=["apple" , "mango" , "water melon" ]
# fruits.append("banana"). #append add something in last
# print(fruits)
# fruits.extend(["jeet" , "aadi"]). #extend add another list in the end
# print(fruits)
#who will pay the bill

# import random
# friends=["aadi" , "jeet" , "nandini" , "diksha"]
# # random1=random.randint(0,4)
# # if random1==0:
# #     print("aadi will pay the bill")
# # elif random1==1:
# #     print("nandini")
# # elif random1==2:
# #     print("jeet")
# # else:
# #     print("diksha")
# print(random.choice(friends))

# friends=["aadi" , "jeet" , "nandini" , "diksha"]
# for friend in friends:
#     print(friend)

# max and inimum function

# score=[150,3,56,70,87,56,25]
# print(max(score))
# print(min(score))

# nums=[1,2,3,4,5,6,7,78,9,1000]
# total=0
# for num in nums:
#     total+=num
# print(total)
# import random
# letters=["a" , "b" , "c" , "d" ,"e" ,"f" ,"g " , "h" , "i" ,"j" ,"k" ,"l" ,"m" ,"n" ,"o" ,"p" ,"q" ,"r" ,"s" ,"t"]
# numbers=["0","1","2","3","4","5","6","7","8","9"]
# symbols=["!" , "@", "#" , "#" ,"$"]
#  print("Welcome to my password generator!")
#  nr_letter= int(input("how many letter you want in password"))
# nr_number=int(input("how many number you wan in your password"))
# nr_symbol=int(input("how many letters"))
#  password=""
#  for char in range(1, nr_letter+1):
#      random_character=random.choice(letters)
#      password+=random_character
#  for char in range(1,nr_symbol+1):
#       password+= random.choice(symbols)
#  for char in range(1, nr_number+1):
#       password+=random.choice(numbers)
#  print(password)
  
# hang man project
# word_bank=["book" , "jeet" , "tiger"]  
# import random
# chosen_word=random.choice(word_bank)
# print(chosen_word)
# guess=input("guess a letter:").lower()
# print(guess)

# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(5) 
# f=open("demo.txt" , "r")
# data=f.read()
# print(data)
# print(type(data))






# jeet="chandradip is great guy"
# print(jeet.replace("a" , "o"))
# print(jeet.find("chandradip"))
# print(jeet.endswith("guy"))
# print(jeet.startswith("chandradip"))

# jeet="chandradip"
# print(jeet.count("c"))
# utt=int(input("enter your units"))
# if utt<=100:
#     print("no charge")
# elif utt>100 and utt<=200:
#     print("your bill is rupees=" , utt*5)
# else:
#     print("your bill =" , utt*10)

# write=int(input("enter your number"))
# xyz=str(write)
# if xyz.endswith("0"):
#     print("divisible")
# elif xyz.endswith("3"):
#     print("diivisibble")
# elif xyz.endswith("6"):
#     print("divisible")
# elif xyz.endswith("9"):
#     print("divisible")
# else:
#     print("not divisible")


#  list
# jeet=["chandradip" , 97, "rishav"]
# print(jeet[1])
# jeet[1]="arjun"
# xyz=(1,2,3,4,5,6,7,)
# print(xyz.sort())

# fact=1
# for i in range(1,6):
#     fact*=i
# print(fact)

# fact=1
# i=1
# while i< 6:
#     i+=1
#     fact*=i
# print(fact)
# dic = { 
#     "name"  : "chandradip",
#     "cgpa" : 10,
#     "marks" : [100, 97,98]
# }
# print(dic["name"])
# print(dic["marks"])
# print(dic["cgpa"])
# dic["name"]="rishav"
# print(dic)
# null_dic={}
# null_dic["name"]="chandradip"
# print(null_dic)

# jeet = { 
#     "name"  : "chandradip",
#     "cgpa" : 10,
#     "marks" : [100, 97,98]
# }
# print(jeet.keys())
# print(jeet.values())
# print(jeet.items())


# collection={1,2,3,4,5,6,"jeet" , "dvi"}
#  collection.add((8,7,6,5,4,3,2,1))
#  print(collection)


# set1={1,2,3,4,5,6}
# set2={4,5,6,7,8,9}
# print(set1.intersection(set2))

# n=5
# print("*" * n)
# print("heello")

# square

# n=int(input("enter your number"))
# for i in range(n):
#     for j in range(4):
#         print("*" , end=" ")
#     print("*")

#  triangle
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*" , end=" ")
#     print()

# decreasing triangle
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print("*" , end=" ")
#     print()
# n=int(input("enter nno of rows"))
# for i in range(n)



#     for j in range(n):
#         print("*" , end =" ")
#     print()

# n=int(input("enter yrows"))
# k=1
# for i in range(1,n+1):
#     for j in range(1,k+1):
#         print("1" , end=" ")
#         k+=2
#     print()

# pyramid
# n=int(input("enter rows")) 
# for i in range(0,n):
#     for j in range(0,n-i-1):
#         print(end=" ")
#     for j in range(0,n):
#         print("*" , end=" ")
#     print()

# down pyramid
# n=int(input("enter rows"))
# for i in range(n ,0,-1):
#     for j in range(0,n-i):
#         print(end=" ")
#     for j in range(0,i):
#         print("*" , end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(n+1):
#         print("*" , end=" ")
#     print()

#WAP to find count the no of vowel in a string
# xyz=str(input("enter your string"))
# print(xyz.count("a"))
# print(xyz.count("e"))
# print(xyz.count("i"))
# print(xyz.count("o"))
# print(xyz.count("u"))

# using loop simplified version

# text=input("enter text")
# vowels='aeiouAEIOU'
# count=0
# for ch in text:
#     if ch in vowels:
#         count+=1
# print(count)


# wap to check if a given string is palindrome or not
# xyz=input("enter string:    ")
# rev=xyz[::-1]
# if xyz==rev:
#     print("yes it is a palindrome")
# else:
#     print("not a palindrome")
# wap to check the no of character in each string
# k=int(input("enter number"))
# i=0
# while i < k:
#     if i==6:
#         continue
#     i+=2
#     print(i)
# num1=int(input("enter number1:  "))
# num2=int(input("enter number2:  "))
# if num1>num2 and (num1 and num2)%2==0:
#     while num2<num1:
#         print(num2)
#         num2+=2
# elif num2>num1 and (num1 and num2)%2==0:
#     while num1 <num2:
#         print(num1)
#         num1+=2
# num1=int(input("enter number: "))
# s=0
# r=0
# while num1!=0:
#     r=num1%10
#     s+=r
#     num1=num1//10
# print(s)
# num1=int(input("enter number: "))
# s=1
# r=0
# while num1!=0:
#     r=num1%10
#     s*=r
#     num1=num1//10
# print(s)
# num1=input('entr number')
# L=list(num1)
# l1=len(L)
# n={0: "zero" , 1: "one" , 2: "two", 3: "three" , 4: "four" , 5: "five" , 6: "six" , 7: "seven" , 8: "eight", 9: "ninne"}
# i=0
# while i < l1:
#     print(n[int(L[i])] , end=" ")
#     i+=1
# n=int(input("enter number"))
# temp=n
# rev=0
# while n>0:
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# if temp==rev:
#     print('number is palindrrome')
# else:
#     print('number is not palindrome')
# L=[]
# i=0
# while i <10:
#     x=int(input("enter number:  "))
#     i+=1
#     L.append(x)
# print(L)
# print( "maximum number is: ", max(L))
# print("minimum number is: ",min(L))
# num=int(input("enter any number"))
# if num==0:
#     print(1)

# else:
#     fact=1
#     while num>0:
#         fact=fact*num
#         num-=1
# print(fact)

# for i in range(200,2000):
#     digit=str(i)
#     power=len(digit)
    
#     output=sum(int(d)**power  for d in digit)
#     if output== i:
#         print(i,"is a amstrong number")
import random 
random_integer=random.randint(0,26)
x=int(input("Guess the number: "))
if x ==random_integer:
    print("exactly right")
elif x > random_integer:
    print("Too high")
else:
    print("Too low")
if x%2==0:
    print("It is a even number:", x)
else:
    print("It is a odd number:", x)


# 
# for length in range(7,0,-2):
#     pattern=""
#     for i in range(length):
#         if i%2==0:
#             pattern+=1
#         else:
#             pattern+=0
#     print(pattern)

# # 
# operators
def sub(n1 , n2):
     return n1- n2

def mul(n1, n2):
     return n1*n2

def div(n1,n2):
     return n1/n2
def add(n1,n2):
    return n1+n2
 # add them in dictionaris as values  keys="+ " , "-"" , "*" , "/"
operations={ 
     "+": add,
     "-":sub,
    "*":mul,
     "/":div,
 }
# use dictionaries for calculations  using dictionaries
print(operations["*"](4,8))

num1=float(input("what is your first number : "))
for symbol in operations:
     print(symbol)
operation_symbol=input("pickup one operator: ")
num2=float(input("what is your second number : "))
print(operations[operation_symbol](num1,num2))

# Three-player Rock-Paper-Scissors-Lizard game

def winner(p1, p2, p3):
    rules = {
        "lizard": "scissors",
        "scissors": "paper",
        "paper": "rock",
        "rock": "lizard"
    }

    players = {"Player1": p1, "Player2": p2, "Player3": p3}
    choices = list(players.values())

    # If all choose the same → Tie
    if len(set(choices)) == 1:
        return "It's a Tie!"

    # Count how many times each weapon chosen
    result = {}
    for name, choice in players.items():
        beats = rules[choice]
        # Count how many players this player beats
        wins = sum(1 for c in choices if c == beats)
        result[name] = wins

    max_wins = max(result.values())
    if list(result.values()).count(max_wins) > 1:
        return "It's a Tie!"
    else:
        winner = max(result, key=result.get)
        return f"{winner} wins using {players[winner]}!"

# Input
p1 = input("Enter Player1 choice (rock/paper/scissors/lizard): ").lower()
p2 = input("Enter Player2 choice (rock/paper/scissors/lizard): ").lower()
p3 = input("Enter Player3 choice (rock/paper/scissors/lizard): ").lower()

print(winner(p1, p2, p3))



import random

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = random.randint(1, 25)

# Identify Even/Odd/Prime
if number % 2 == 0:
    kind = "Even"
else:
    kind = "Odd"
if is_prime(number):
    kind += " and Prime"

print("Guess a number between 1 and 25!")
while True:
    guess = int(input("Enter your guess: "))
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! The number was", number)
        print("It is:", kind)
        break


def convert(num, dtype):
    if dtype == "binary":
        return bin(int(num))
    elif dtype == "octal":
        return oct(int(num))
    elif dtype == "hexadecimal":
        return hex(int(num))
    else:
        return num

print("Choose data type: decimal, float, binary, octal, hexadecimal")
dtype = input("Enter data type: ").lower()

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose operation: +, -, *, /")
op = input("Enter operation: ")

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    print("Invalid operation!")
    result = None

if result is not None:
    print("Result =", convert(result, dtype))


# Pattern printing

n = 7
while n >= 1:
    for i in range(n):
        print("1" if i % 2 == 0 else "0", end="")
    print()
    n -= 2