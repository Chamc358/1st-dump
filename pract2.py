import math

def speed_calculator():
    distance = int(input("Distance travelled in km: "))
    time = int(input("How long was the journey in hours: "))
    
    print(distance / time)
    
def circumference_of_circle():
    radius = float(input("Enter radius of circle: "))
    print(2 * math.pi * radius)
    
    
def area_of_circle():
    radius = float(input("Enter radius of circle: "))
    print(math.pi * radius**2)

def cost_of_pizza():
    diameter = float(input("Enter diameter in cm: "))
    radius = diameter / 2
    area = math.pi * radius**2
    cost = (3.5 * area) / 100
    print(round(cost, 2))
    
def slope_of_line():
    x_1 = float(input("Enter x_1 value: "))
    y_1 = float(input("Enter y_1 value: "))
    x_2 = float(input("Enter x_2 value: "))
    y_2 = float(input("Enter y_2 value: "))
    
    print((y_2 - y_1)/(x_2 - x_1))
    
def distance_between_points():
    x_1 = float(input("Enter x_1 value: "))
    y_1 = float(input("Enter y_1 value: "))
    x_2 = float(input("Enter x_2 value: "))
    y_2 = float(input("Enter y_2 value: "))
    
    distance = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)
    print(distance)
    
def travel_statistics():
    avg_speed = float(input("Enter avg speed in km/h: "))
    duration = float(input("Enter num of hours: "))
    
    distance = avg_speed * duration
    fuel = distance / 5
    print("Distance travelled: ", distance)
    print("Fuel used: ", fuel)
    
def sum_of_squares():
    n = int(input("Ending num: "))
    total = 0
    for i in range(n+1):
        square = i**2
        total += square
    print(total)
    
def average_of_numbers():
    num_items = int(input("How many numbers will be inputted: "))
    total = 0
    for i in range(num_items):
        numbers = int(input("Enter numbers: "))
        total += numbers
    print(total / num_items)

def fibonacci():
    nth = int(input("Enter a number: "))
    
    first_num = 0
    second_num = 1
    
    for _ in range(nth):
        next_num = first_num + second_num
        first_num = second_num
        second_num = next_num
    
    print(first_num)
        
def select_coins():
    money = int(input("Enter number of pennies: "))
    
    two_pound = money // 200
    money %= 200
    
    one_pound = money // 100
    money %= 100
    
    fifty_pence = money // 50
    money %= 50
    
    twenty_pence = money // 20
    money %= 20
    
    ten_pence = money // 10
    money %= 10
    
    five_pence = money // 5
    money %= 5
    
    two_pence = money // 2
    money %= 2
    
    one_pence = money // 1
    money %= 1
    
    print(two_pound, "* £2,", one_pound, "* £1,",
          fifty_pence,"* 50p",twenty_pence, "* 20p",
          ten_pence, "* 10p",five_pence, "* 5p",
          two_pence, "* 2p",one_pence, "* 1p",)
    
    
def select_coins_2():
    amount = int(input("Enter number of pennies: "))
    
    coin_selection = [200, 100, 50, 20, 10, 5, 2, 1]
    coin_names = ["£2", "£1", "50p", "20p", "10p", "5p", "2p", "1p"]
    
    coins = []
    
    for i in coin_selection:
        number = amount // i
        amount %= i
        coins.append(number)
        
    for i in range(len(coin_names)):
        print(coin_names[i], "*", coins[i])
        