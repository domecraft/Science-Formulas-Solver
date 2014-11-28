puts "This program will solve for systems of equations"
puts "Does your system have two or three variables?"
numOfVariables = gets.chomp.to_i
if (numOfVariables == 2)
	puts "Enter X for first equation"
	x1 = gets.chomp.to_f
	puts "Enter Y for first equation"
	y1 = gets.chomp.to_f
	puts "What is the equation equal to?"
	equals1 = gets.chomp.to_f
	puts "Enter X for second equation"
	x2 = gets.chomp.to_f
	puts "Enter Y for second equation"
	y2 = gets.chomp.to_f
	puts "What is the equation equal to?"
	equals2 = gets.chomp.to_f

	determinant = (x1 * y2) - (y1 * x2)
	determinantX = (equals1 * y2) - (y1 * equals2)
	determinantY = (x1 * equals2) - (equals1 * x2)

	x = determinantX / determinant
	y = determinantY / determinant
	if ((!x.nan?) || (!y.nan?)) #check if there are infinite solutions  
		puts "The value of x is: #{x}"
		puts "The value of y is: #{y}"
	else
		puts "infininite # of solutions"
	end


	
elsif (numOfVariables == 3)
	puts "Enter the first equation"
	
else
	puts "lolwut"
end
