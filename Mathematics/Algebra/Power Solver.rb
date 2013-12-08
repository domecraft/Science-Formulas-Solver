#This program will solve for the powers and loops through the range that the user enters.

puts "Enter the minimum value of the loop"
min = gets.chomp
min = min.to_i
puts "Enter the maximum value of the loop"
max = gets.chomp
max = max.to_i
puts "Enter the power you want to apply to each number"
power = gets.chomp
power = power.to_i
(min..max).each do|x| 
    print "#{x}: ", x**power, " "
    puts ""
end
