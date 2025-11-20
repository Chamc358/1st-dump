def input_number(prompt):
    n = int(input(prompt))
    return n

def square_number(number):
    return number ** 2

def output_result(info):
    print(info)

def main():
    n = input_number("Woo!Hoo!")
    result = square_number(n)
    print(result)
    
main()