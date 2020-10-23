from decimal import Decimal, getcontext

a = int(input("Enter the value of a in your linear equation: "))
b = int(input("Enter the value of b in your linear equation: "))
factor = -(b/a)
print("The root of that linear equation is", factor)
print()
print("Do you want more decimal digits of your root? (Y/N)")
choice = input()

if choice == "Y":
  print("How many digits of the root you want? ")
  nd = int(input())
  getcontext().prec = nd + 1
  print(Decimal(factor))
elif choice == "N":
  print("Have a nice day. Goodbye")
