#Variables
#import math as m
pi = 3.142

#circle_area function:
def circle_area():
    try:
        r = int(input())
        return pi*r**2
    except:
        return "error"

#circle_circ function:
def circle_circ():
    try:
        r = int(input())
        return 2*pi*r
    except:
        return "error"

#square_area funtion:
def square_area():
    try:
        l = int(input())
        w = int(input())
        return (l**2)*w
    except:
        return "error"

#square_perimeter function:
def square_perimeter():
    try:
        l = int(input())
        return l*4
    except:
        return "error"

#cube_volume function:
def cube_volume():
    try:
        l = int(input())
        w = int(input())
        h = int(input())
        return l*w*h
    except:
        return "error"

#cube_area function:
def cube_area():
    try:
        l = int(input())
        w = int(input())
        h = int(input())
        return 2*w*l+2*l*h+2*h*w
    except:
        return "error"


#Main code:
while True:
    type = input("Type of shape: (h : help)(q : quit)")
    calc = input("Enter the calculation you wish to perform on said shape")
    calc_performed = False

    if type.lower() == "circle":
        if calc.lower() == "area":
            result = circle_area()
            calc_performed = True
        elif calc.lower() == "circumference":
            result = circle_circ()
            calc_performed = True
        else:
            print("Invalid format")
    elif type.lower() == "square":
        if calc.lower() == "area":
            result = square_area()
            calc_performed = True
        elif calc.lower() == "perimeter":
            result = square_perimeter()
            calc_performed = True
        else:
            print("Invalid format")
    elif type.lower() == "cuboid":
        if calc.lower() == "volume":
            result = cube_volume()
            calc_performed = True
        elif calc.lower() == "area":
            result = cube_area()
            calc_performed = True
        else:
            print("Invalid format")
    elif type.lower() == "h":
        print("""Operation of the program is simple:
        1) Enter the shape you want to perform the operation on.
        2) Select the operation
        3) Enter your values
        You have successfully performed an operation.""")
    elif type.lower() == "q":
        quit()
    else:
        print("Invalid entry")
    if result == "error":
        print("Error was raised")
    else:
        print(f"Result is: {result}")