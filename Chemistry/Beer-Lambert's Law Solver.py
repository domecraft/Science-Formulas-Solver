print"This program will solve for epsilon in beer-lambert's law"
slope=raw_input('Enter the slope of the line')
slope=float(slope)
length=raw_input('Enter the length of the cuvette')
length=float(length)
epsilon=slope/length
epsilon=str(epsilon)
print "The epsilon for the equation is: " + epsilon
