# # operators
# def sub(n1 , n2):
#     return n1- n2

# def mul(n1, n2):
#     return n1*n2

# def div(n1,n2):
#     return n1/n2
# def add(n1,n2):
#     return n1+n2
# # add them in dictionaris as values  keys="+ " , "-"" , "*" , "/"
# operations={ 
#     "+": add,
#     "-":sub,
#     "*":mul,
#     "/":div,
# }
# # use dictionaries for calculations  using dictionaries
# print(operations["*"](4,8))

# num1=float(input("what is your first number : "))
# for symbol in operations:
#     print(symbol)
# operation_symbol=input("pickup one operator: ")
# num2=float(input("what is your second number : "))
# print(operations[operation_symbol](num1,num2))
for length in range(7, 0, -2):   # lengths will be 7, 5, 3, 1
    pattern = ""                 # start with an empty string
    for i in range(length):      # generate alternating 1s and 0s
        if i % 2 == 0:           # even position
            pattern += "1"
        else:                    # odd position
            pattern += "0"
    print(pattern)               # print the line