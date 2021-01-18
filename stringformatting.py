"""
Author: Pang Jin Jia
Last updated: 18 Jan 2021

this is an example file that shows the different ways to print the same statement out
"""

a = 11
b = 18
c = 30
d = (a+b+c)//3

print("The answer is " + str(d))

print("The answer is",d)

print("The answer is ",end="")
print(d)

print(f"The answer is {d}")

print("The answer is %d" % (d))

print("The answer is {}".format(d))
