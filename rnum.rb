
inputint = 1
stop = false
while stop == false do
  puts "Enter a number"
  inputint = gets.chomp.to_i
  if inputint == 0
    stop = true
  end
  x = ""
  while inputint>0
    if inputint-100==0
      x << "C"
      inputint=inputint-100

    elsif inputint-90>=0
      inputint=inputint-90
      x << "XC"

    elsif inputint-50>=0
      x << "L"
      inputint=inputint-50

    elsif inputint-40>=0
      x << "XL"
      inputint=inputint-40

    elsif inputint-10>=0
      x << "X"
      inputint=inputint-10

    elsif inputint-9>=0
      x << "IX"
      inputint=inputint-9

    elsif inputint-5>=0
      x << "V"
      inputint=inputint-5

    elsif inputint-4>=0
      x << "IV"
      inputint=inputint-4

    elsif inputint-1>=0
      x << "I"
      inputint=inputint-1

    end
  end
  if stop == false
    puts x
  end
end

# 100
# 90
# 50
# 40
# 10
# 9
# 5
# 4
# 1