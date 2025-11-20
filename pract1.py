def say_name():
    name = input("What is your name? ")
    return name

def say_hello_2():
    print("hello\nworld")
    
def dollars_to_pounds():
    money_amount = float(input("Please enter how many dollars you have: "))
    amount = money_amount * 1.35
    print("You have £",round(amount, 2))
       
def sum_and_difference():
    num1 = int(input("Please enter your first number: "))
    num2 = int(input("Please enter your second number: "))
    
    total = num1 + num2
    print(total)
    
    difference = num1 - num2
    print(difference)
    
def change_counter():
    oneps = int(input("How many 1p's do you have: "))
    twops = int(input("How many 2p's do you have: "))
    fiveps = int(input("How many 5p's do you have: "))
    
    twops = twops * 2
    fiveps = fiveps * 5
    
    total = oneps + twops + fiveps
    print(total)
    
def ten_hellos():
    for i in range(11):
        print("Hello World")
        
def zoom_zoom():
    number = int(input("Please enter a number: "))
    for i in range(1, number+1):
        print("zoom", i)
        
def count_to():
    number = int(input("Please enter a number: "))
    for i in range(number+1):
        print(i)
        
def count_from_to():
    start = int(input("Please enter your starting number: "))
    end = int(input("Please enter your final number: "))
    for i in range(start, end+1):
        print(i)

def weights_table():
    kgToOunce = 35.27
    for i in range(10, 110, 10):
        print(i, kgToOunce*i)
    
def future_value():
    start = float(input("Please enter your starting amount: "))
    years = int(input("Please enter the number of years you will be investing for: "))
    
    interest = 1.035
    counter = 0    
        
    for counter in range(years):
        start = start * interest
        print(round(start, 2))
