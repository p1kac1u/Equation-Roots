#!/usr/bin/env python3

'''
MIT LICENSE

Copyright 2020 p1kac1u
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
from decimal import Decimal, getcontext

a = Decimal(input("Enter the value of a in your linear equation: "))
b = Decimal(input("Enter the value of b in your linear equation: "))
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
