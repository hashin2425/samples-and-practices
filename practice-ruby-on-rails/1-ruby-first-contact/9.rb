# dict
dictionaly = {
    "name" => "John",
    "age" => 30,
}

puts dictionaly["name"]
puts dictionaly["address"] # 存在しないのでnilが返る
puts dictionaly.fetch("address", "default value") # 存在しない場合のデフォルト値を指定できる
puts dictionaly.values, dictionaly.keys, dictionaly.length

dictionaly.each do |key, value|
    puts "#{key}: #{value}"
end

# defaultdictみたいなやつ
dict1 = Hash.new(1)
dict1["key"] = 2
puts dict1["num"] # 存在しないのでデフォルト値が返る

