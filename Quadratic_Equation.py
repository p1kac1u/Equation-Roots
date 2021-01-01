from decimal import Decimal, getcontext
import math

# Obtaining quadratic equation information from the user
a = Decimal(input("Enter the value of the coefficient a in your quadratic eqaution: "))
b = Decimal(input("Enter the value of the coefficient b in your quadratic eqaution: "))
c = Decimal(input("Enter the value of the coefficient c in your quadratic eqaution: "))

# Defining a function for calculating the roots
def quadraticsolver(a,b,c):
    dis = (b ** 2) - 4 * a * c # Calculating the discriminant
    sqrt_dis = Decimal(math.sqrt(abs(dis)))
    
    # Checking the condition of the discriminant
    if dis >= 0:
        root_1 = (-b + sqrt_dis) / (2 * a)
        root_2 = (-b - sqrt_dis) / (2 * a)
        print("The first root is", root_1)
        print("The second root is", root_2)
    elif dis < 0:
        root_1 = (-b + sqrt_dis) / (2 * a)
        root_2 = (-b - sqrt_dis) / (2 * a)
        print("The first root is", root_1, "i")
        print("The second root is", root_2, "i")

def moredecimal():
    # More Decimal digits
    print()
    print("Do you want more decimal digits of your root? (Y/N)")
    choice = input()

    if choice == "Y":
        dis = (b ** 2) - 4 * a * c # Calculating the discriminant
        sqrt_dis = Decimal(math.sqrt(abs(dis)))
        print("How many digits of the root you want? ")
        nd = int(input())
        getcontext().prec = nd + 1
        if dis >= 0:
            root_1 = Decimal((-b + sqrt_dis) / (2 * a))
            root_2 = Decimal((-b - sqrt_dis) / (2 * a))
            print("The first root is", root_1)
            print("The second root is", root_2)
        elif dis < 0:
            root_1 = Decimal((-b + sqrt_dis) / (2 * a))
            root_2 = Decimal((-b - sqrt_dis) / (2 * a))
            print("The first root is", root_1, "i")
            print("The second root is", root_2, "i")
    elif choice == "N":
        print("Have a nice day. Goodbye")
    elif choice != "Y" or "N":
        print("Err! Your choice went over my head. Please try again.")
        moredecimal()
        
if a == 0:
    print("The quadratic equation that you have entered is incorrect. Please try again.")
else:
    quadraticsolver(a,b,c)
    moredecimal()
