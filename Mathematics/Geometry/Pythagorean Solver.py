print"This program will solve the pythagorean theorem for you"
unit=raw_input('Enter the unit you will be using')
a=raw_input('Enter the length of side a')
if a<0:
  print"A cannot be less than zero"
else
a=float(a)
b=raw_input('Enter the length of side b')
if b<0:
  print"B cannot be less than zero"
else
b=float(b)
c2=(a**2)+(b**2)
c=math.sqrt(c2)
print "The length of side C is: "+ c + " " + unit + "."
