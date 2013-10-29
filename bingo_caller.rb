#Author: Theron Boerner
#Filename: bingo_caller.rb

numbers = []

5.times do |number|
  small_array = []
  15.times do |number1|
    small_array.push((number * 15) + number1 + 1)
  end
  small_array.shuffle!
  numbers.push(small_array)
end
numbers.shuffle!

called = []

input = ""
while !(input.downcase == "end")
  input = gets.chomp
  if input.downcase == "called"
    puts called.sort
    input = ""
  else
    x = rand(numbers.size)
    begin
      y = rand(numbers[x].size)
    rescue NoMethodError
      break
    end
    output = numbers[x][y]
    numbers[x].delete(output)
    if numbers[x].size == 0
      numbers.delete_at(x)
    end
    output_s = ""
    case output
    when 1..15
      output_s << "B"
    when 16..30
      output_s << "I"
    when 31..45
      output_s << "N"
    when 46..60
      output_s << "G"
    when 61..75
      output_s << "O"
    end
    output_s << output.to_s
    called.push(output_s)
    puts output_s
  end
end