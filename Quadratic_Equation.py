import math

# Obtaining quadratic equation information from the user
a = int(input("Enter the value of the coefficient a in your quadratic eqaution: "))
b = int(input("Enter the value of the coefficient b in your quadratic eqaution: "))
c = int(input("Enter the value of the coefficient c in your quadratic eqaution: "))

# Defining a function for calculating the roots
def quadraticsolver(a,b,c):
    dis = (b ** 2) - 4 * a * c # Calculating the discriminant
    sqrt_dis = math.sqrt(abs(dis))
    
    # Checking the condition of the discriminant
    if dis >= 0:
        print("The first root is", (-b + sqrt_dis) / (2 * a))
        print("The second root is", (-b - sqrt_dis) / (2 * a))
    elif dis < 0:
        print("The first root is", (-b + sqrt_dis) / (2 * a), "i")
        print("The second root is", (-b - sqrt_dis) / (2 * a), "i")
if a == 0:
    print("The quadratic equation that you have entered is incorrect. Please try again.")
else:
    quadraticsolver(a,b,c)
