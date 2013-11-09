import math
print " This program will find the binomials of an equation."
a = int(raw_input('Enter the first coefficient'))
b = int(raw_input('Enter the second coefficient'))
c = int(raw_input('Enter the third term'))
firstbinomial=str(int((((b*-1)+math.sqrt((b**2)-(4*a*c)))/(2*a))*-1))
secondbinomial=str(int((((b*-1)-math.sqrt((b**2)-(4*a*c)))/(2*a))*-1))  
print"The binomials are: (x"+firstbinomial+")(x"+secondbinomial")"
