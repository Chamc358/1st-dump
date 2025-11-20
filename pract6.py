import math
import random
from graphix import Circle, Window, Point, Line, Text
from pract5 import distance_between_points


def greet(name):
    print("Hello", name + ".")
    if len(name) > 20:
        print("That's a long name!")


def can_you_vote(age):
    if age >= 18:
        print("You can vote")
    else:
        print("Sorry, you can't vote")


def get_degree_class(mark):
    if mark >= 70:
        return "1st"
    elif mark >= 60:
        return "2:1"
    elif mark >= 50:
        return "2:2"
    elif mark >= 40:
        return "3rd"
    else:
        return "Fail"


# We will simplify this function later in the term
def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def days_in_month(month, year):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 31


def overly_complex_days_in_month(month, year):
    if month == 1 or month == 3 or month == 5 or month == 7 or \
       month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif is_leap_year(year):
        return 29
    else:
        return 28


def count_down():
    for i in range(10, 0, -1):
        print(i, "...", end=" ")
    print("Blast Off!")


def numbered_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    
    
def fast_food_order_price():
    price = float(input("Enter the price of your meal: "))
    
    if price < 20:
        price += 2.50
        print("The total price of your order is", price)
    
    elif price > 20:
        print("The total price of your order is", price)
        
        
def what_to_do_today():
    temp = float(input("What is the temperature today?: "))
    
    if temp > 25:
        print("Swim in the sea")
    elif temp < 25 and temp > 10:
        print("Go shopping in Gunwharf Quays")
    else:
        print("Watch a film at home")
        

def display_square_roots(start, end):
    for i in range(start, end):
        print("The square root of", i, "is", round(math.sqrt(i), 3))
    

def calculate_grade(mark):
    if mark > 20 or mark < 0:
        print("X")
    elif mark >= 16:
        print("A")
    elif mark < 16 and mark >= 12:
        print("B")
    elif mark < 12 and mark >= 8:
        print("C")
    else:
        print("F")


def peas_in_a_pod():
    num = int(input("Enter num of peas: "))
    
    win = Window("Pod", num * 100, 100)
    
    for x in range(0, num*100, 100):
        centre = Point(x + 50, 50)
        peas = Circle(centre, 50)
        peas.draw(win)
        peas.fill_colour = "light green"
    
    win.get_mouse()
    win.close()
    
    
def ticket_price(distance, age):
    total = 0
    cost = 10
    distance_cost = 0.15 * distance
    
    if age >= 60 or age <= 15:
        total = round((distance_cost + cost) * 0.6, 3)
        print(total)
    else:
        total = round(cost + distance_cost, 3)
        print(total)


def numbered_square(n):
    for row in range(n):
        start = n - row           
        for col in range(n):       
            print(start + col, end = " ")
        print()
        

def draw_circle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.fill_colour = colour
    circle.draw(win)
    

def draw_patch_window():
    win = Window("Patch work", 200, 200)
    
    start_pos = Point(0, 100)
    end_pos = Point(0,100)
    
    second_start = Point(100, 0)
    second_end = Point(100, 0)
    
    third_start = Point(0, 0)
    third_end = Point(0, 0)
    
    fourth_start = Point(100, 100)
    fourth_end = Point(100, 100)
    
    for i in range(0, 100, 20):
        start_pos.move(0, -20)
        end_pos.move(20, 0)
        
        second_start.move(-20, 0)
        second_end.move(0, 20)
        
        third_start.move(0, 20)
        third_end.move(20, 0)
        
        fourth_start.move(-20, 0)
        fourth_end.move(0, -20)
        
        lin1 = Line(start_pos, end_pos)
        lin1.draw(win)
        lin1.fill_colour = "red"
        
        lin2 = Line(second_start, second_end)
        lin2.draw(win)
        lin2.fill_colour = "red"
        
        lin3 = Line(third_start, third_end)
        lin3.draw(win)
        lin3.fill_colour = "red"
        
        lin4 = Line(fourth_start, fourth_end)
        lin4.draw(win)
        lin4.fill_colour = "red"
    
    

    win.get_mouse()
    win.close()


#def draw_patch(win, x, y, colour):
    


"""
def draw_patchwork():
    win = Window("Patchwork", 300, 200)
    
    for i in range(0, 300, 100):
        draw_patch(win, 0, 0, "blue")
    
    win.get_mouse()
    win.close()
"""

def draw_coloured_eye(win, centre, radius, colour):
    draw_circle(win, centre, radius, colour)
    draw_circle(win, centre, int(radius * 0.5), colour)
    draw_circle(win, centre, int(radius * 0.25), colour)
    
    
def eye_picker():
    win = Window("Eye picker", 400, 400)
    
    x = int(input("Enter the x coordinate of the centre: "))
    y = int(input("Enter the y coordinate of the centre: "))
    
    centre = Point(x, y)
    
    colours = ["blue", "grey", "green", "brown"]
    colour = input("Enter the colour of circle: ")
    
    if x > 400 or x < 0:
        print("Eye centre not in window")
    elif y > 400 or y < 0:
        print("Eye centre not in window")
    else:
        if colour not in colours:
            print("not a valid eye colour")
        else:
            draw_coloured_eye(win, centre, 30, colour)
            
            win.get_mouse()
            win.close()
      

def eyes_all_around():
    win = Window("Eyes", 500, 500)
    colours = ["green", "blue", "brown", "grey"]
    
    for i in range(30):
        centre = win.get_mouse()
        for i in colours():
            draw_coloured_eye(
            
    
    
    
def draw_archery_target():
    yellow_radius = 100
    red_radius = 200
    blue_radius = 300
    
    MAX = 800
    
    win = Window("New Window", MAX, MAX)
    centre = Point(MAX // 2, MAX // 2)
    
    cir1 = Circle(centre, blue_radius)
    cir1.draw(win)
    cir1.fill_colour = "blue"
    
    cir2 = Circle(centre, red_radius)
    cir2.draw(win)
    cir2.fill_colour = "red"
    
    cir3 = Circle(centre, yellow_radius)
    cir3.draw(win)
    cir3.fill_colour = "yellow"
    
    score = 0
    
    for i in range(5):
        adjustment_x = random.randint(-200, 200)
        adjustment_y = random.randint(-200, 200)
        
        click = win.get_mouse()
        dx = click.x + adjustment_x
        dy = click.y + adjustment_y
        
        d = distance_between_points(Point(dx, dy), centre)
        
        if d <= yellow_radius:
            score += 10
            
        elif d <= red_radius:
            score += 5
            
        elif d <= blue_radius:
            score += 2
            
        else:
            score + 0
            
        
        black_cir = Circle(Point(dx, dy), 5)
        black_cir.draw(win)
        black_cir.fill_colour = "black"
        
    result = Text(Point(400, 30), "Your score was: " + str(score))
    result.size = 20
    result.draw(win)
    
    win.get_mouse()
    win.close()


    
    
    
    
    
    
