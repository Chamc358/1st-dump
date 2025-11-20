import math
from graphix import Window, Circle, Point, Text, Line


def greet(name):
    return f"Hello, {name}!"


def product(a, b):
    return a * b


def divide(a, b):
    return a / b


def divide_and_product(a, b):
    product_result = product(a, b)
    divide_result = divide(a, b)
    return product_result, divide_result


def main():
    my_name = input("What is your name? ")
    greeting = greet(my_name)
    print(greeting)

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    product_result, divide_result = divide_and_product(num1, num2)
    print(f"{num1} * {num2} = {product_result}")
    print(f"{num1} / {num2} = {divide_result}")


def calc_future_value(amount, years):
    interest_rate = 0.065
    for year in range(years):
        amount = amount * (1 + interest_rate)
    return amount


def future_value():
    amount = float(input("Enter an amount to invest: "))
    years = int(input("Enter the number of years: "))
    final = calc_future_value(amount, years)

    output = f"Investing £{amount:0.2f} for {years} years "
    output += f"results in £{final:0.2f}."
    print(output)


def area_of_circle(radius):
    return math.pi * radius ** 2


def draw_circle(win, centre, radius, colour):
    circle = Circle(centre, int(radius))
    circle.fill_colour = colour
    circle.outline_width = 2
    circle.draw(win)


def draw_brown_eye(win, centre, radius):
    draw_circle(win, centre, radius, "white")
    draw_circle(win, centre, int(radius * 0.5), "brown")
    draw_circle(win, centre, int(radius * 0.25), "black")
    
    
def draw_pair_of_brown_eyes():
    MAX = 400
    win = Window("Pair of brown eyes", MAX, MAX)
    
    left_eye_centre = Point(130, 200)
    right_eye_centre = Point(270, 200)
    
    draw_brown_eye(win, left_eye_centre, 70)
    draw_brown_eye(win, right_eye_centre, 70)
    
    win.get_mouse()
    win.close()
    
    
def circumference_of_circle(radius):
    return 2 * math.pi * radius


def circle_info():
    radius = float(input("Enter radius: "))
    print("The area is ", round(area_of_circle(radius), 3), "and the circumference is ", round(circumference_of_circle(radius), 3))
    
    
def draw_brown_eye_in_centre():
    MAX = 400
    win = Window("New Window", MAX, MAX)
    
    centre = Point(200, 200)
    
    
    draw_circle(win, centre, 120, "white")
    draw_circle(win, centre, 60, "brown")
    draw_circle(win, centre, 30, "black")
        
    win.get_mouse()
    win.close()


def draw_block_of_stars(width, height):
    for _ in range(height):
        print("*" * width)
        

def draw_letter_e():
        draw_block_of_stars(8, 2)
        draw_block_of_stars(2, 2)
        draw_block_of_stars(8, 2)
        draw_block_of_stars(2, 2)
        draw_block_of_stars(8, 2)


def distance_between_points(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    answer = math.sqrt(dx**2 + dy**2)
    return answer

p1 = Point(100, 50)
p2 = Point(30, 80)


def distance_calculator(p1, p2):
    MAX = 400
    win = Window("New Window", MAX, MAX)
    
    instruction = Text(Point(200, 30), "Click on 2 locations")
    instruction.size = 25
    instruction.draw(win)
    
    p1 = win.get_mouse()
    p2 = win.get_mouse()
    
    distance = distance_between_points(p1, p2)
    instruction.undraw()
    
    instruction = Text(Point(200, 30), str(distance))
    instruction.size = 25
    instruction.draw(win)
    
    win.get_mouse()
    win.close()


def draw_four_pairs_of_brown_eyes():
    
    win = Window("4 pairs of eyes", 1200, 600)
    
    for _ in range(4):
        left_eye_centre = win.get_mouse()
        p2 = win.get_mouse()
        
        radius = distance_between_points(left_eye_centre, p2)
        draw_brown_eye(win, left_eye_centre, radius)
        
        right_eye_centre = Point(left_eye_centre.x + int(radius * 3), left_eye_centre.y)
        draw_brown_eye(win, right_eye_centre, radius)
        
        
    win.get_mouse()
    win.close()
    

def display_text_with_spaces(string, size, position, win):
    spaced_word = " ".join(string.upper())
    word = Text(position, spaced_word)
    word.size = size
    word.draw(win)
    
    
def construct_vision_chart():
    MAX = 400
    win = Window("Vision Chart", MAX, MAX)
    
    size = 35
    position = Point(200, 30)

    for _ in range(6):
        size -= 5
        position.move(0, 50)
        word = input("Enter a string: ")
        
        display_text_with_spaces(word, size, position, win)
    
    win.get_mouse()
    win.close()
    
    
def draw_stick_figure(win, position, size):
    x = position.x
    y = position.y
    
    head_radius = int(size)
    head = Circle(Point(x, y), head_radius)
    head.draw(win)
    
    top_body = Point(x, y + head_radius)
    bottom_body = Point(x, y + head_radius + int(size * 2))
    body = Line(top_body, bottom_body)
    body.draw(win)
    
    arm_y = y + head_radius + int(size * 0.75)
    arms = Line(Point(x - size, arm_y), Point(x + size, arm_y))
    arms.draw(win)
    
    left_leg = Line(bottom_body, Point(x - size, y + head_radius + size * 3))
    right_leg = Line(bottom_body, Point(x + size, y + head_radius + size * 3))
    right_leg.draw(win)
    left_leg.draw(win)
    
    
def draw_stick_figure_family():
    win = Window("Stick Figure Family", 600, 400)
    
    for _ in range(5):
        position = win.get_mouse()
        size_point = win.get_mouse()
        dx = size_point.x - position.x
        dy = size_point.y - position.y
        size = int(math.sqrt(dx**2 + dy**2))
        
        draw_stick_figure(win, position, size)
        
    win.get_mouse()
    win.close()
    
