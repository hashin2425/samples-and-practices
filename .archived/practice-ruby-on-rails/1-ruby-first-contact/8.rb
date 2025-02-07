something_list = [1, 2, 3, 4, 5, "six", "seven", "eight", "nine", "ten"]

something_list[0] = "one"

puts something_list[0]
puts something_list.at(6)
puts something_list[-1]
puts something_list.length
puts something_list.count{|item| !item.is_a?(String)}

# 第一引数の長さで、第二引数で埋める
empty_list = Array.new(10, "num")
empty_list = ["num"] * 10 # これでも同じ
puts empty_list

something_list.each do |item|
    puts item
end
