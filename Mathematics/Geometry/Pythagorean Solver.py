import math
print"This program will solve the pythagorean theorem for you"
unit=raw_input('Enter the unit you will be using')
a=raw_input('Enter the length of side a')
a=float(a)
if a<0:
  print"A cannot be less than zero"
else:
    b=raw_input('Enter the length of side b')
    b=float(b)
if b<0:
  print"B cannot be less than zero"
else:
    c2=(a**2)+(b**2)
    c=math.sqrt(c2)
    c=str(c)
    print "The length of side C is: "+ c + " " + unit + "."
