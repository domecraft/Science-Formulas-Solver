import math
print"This program will solve the pythagorean theorem for you"
unit=raw_input('Enter the unit you will be using: ')
a=float(raw_input('Enter the length of side a: '))
if a<0:
  print"A cannot be less than zero"
else:
    b=float(raw_input('Enter the length of side b: '))
    if b<0:
        print"B cannot be less than zero"
    else:
        c=str(math.sqrt((a**2)+(b**2)))
        print "The length of side C is: "+ c + " " + unit + "."
    
