#Author: Theron Boerner
#Filename: bingo.rb

header = ["b","i","n","g","o"]
string_to_print = "   "
new_line = "*" * 32
seperator = "*" * 2
random_numbers = []
header.each do |element|
  string_to_print << "#{element}     "
end
string_to_print << "\n"
string_to_print << new_line + "\n"

5.times do |number|
  array = []
  5.times do
    rand_num = rand(((number * 15) + 1)..((number * 15) + 15))
    while array.include? rand_num
      rand_num = rand(((number * 15) + 1)..((number * 15) + 15))
    end
    array.push(rand_num)
  end
  random_numbers.push(array)
end

5.times do |x|
  string_to_print << seperator
  5.times do |y|
    if y == 0
      space = " "
    end
    if random_numbers[y][x].to_s.length < 2
      space << " "
    end
    string_to_print << "#{space}"
    if x == 2 && y == 2
      string_to_print << "FS"
    else
      string_to_print << "#{random_numbers[y][x]}"
    end
    string_to_print << " #{seperator} "
  end
  string_to_print << "\n#{new_line} \n"
end

puts string_to_print