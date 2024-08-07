MAX = 9

# while 条件式がTrueのうちは繰り返す
num = 1
while num <= MAX do # doは省略可能
    print num
    num += 1
end
puts ""

# until 条件式がFalseの間繰り返す
num = 1
until num > MAX do
    print num
    num += 1
end
puts ""

# for 両端も含まれる
for num in 1..MAX do
    print num
end
puts ""

# 数列を作るやつ（PythonのRangeと同じように、ジェネレータが作られるイメージ？）
puts 1..MAX # 1以上MAX以下
puts 1...MAX # 1以上MAX未満
puts Range.new(1, MAX)

# each
(1..MAX).each do |num|
    print num
end
puts ""

(1..MAX).each{|num|
    print num
}
puts ""

# times {整数値}回数だけ繰り返す
MAX.times do |num|
    print num + 1
end
puts ""

# upto
1.upto(MAX) do |num|
    print num
end
puts ""

# downto
MAX.downto(1) do |num|
    print num
end
puts ""

# step 1からMAXまで2ずつ増やしていく。Pythonのrange(1, MAX, 2)と同じ。浮動小数点数OK
1.step(MAX, 2) do |num|
    print num
end
puts ""

# loop 無限ループ
num = 1
loop do
    num += 1
    next if num % 2 == 0 # nextでスキップ
    break if num > MAX
    print num
end
puts ""

# redo ループの最初に戻る
10.times do |num|
    random_num = rand(10)
    redo if random_num % 2 == 0
    print random_num
end
puts ""

# 式修飾子
num = 1
print num += 1 while num < MAX
puts ""

num = 1
print num += 1 until num > MAX
puts ""
