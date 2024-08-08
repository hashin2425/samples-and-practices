MINIMUM_NUM = 1
MAXIMUM_NUM = 999

result_num = rand(MINIMUM_NUM..MAXIMUM_NUM)

def get_input_as_number
    return gets.chomp.to_i
end

loop do
    print "Enter number: "
    input_num = get_input_as_number

    if input_num == result_num
        puts "You win!"
        break
    elsif input_num > result_num
        puts "Too high"
    else
        puts "Too low"
    end
end
