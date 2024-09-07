# Ruby基本構文まとめ

# 1. コメント
# これは単一行コメントです

=begin
これは
複数行コメント
です
=end

# 2. 変数と定数
variable = "これは変数です"
CONSTANT = "これは定数です"

# 3. データ型
# 3.1 数値
integer = 42
float = 3.14

# 3.2 文字列
string = "これは文字列です"
interpolation = "文字列補間: #{variable}"

# 3.3 配列
array = [1, 2, 3, 4, 5]

# 3.4 ハッシュ
hash = { "key" => "value", :symbol_key => "another value" }

# 3.5 シンボル
symbol = :this_is_a_symbol

# 4. 条件分岐
# 4.1 if文
if true
  puts "条件は真です"
elsif false
  puts "この条件は偽です"
else
  puts "どの条件にも一致しません"
end

# 4.2 unless文
unless false
  puts "条件は偽です"
end

# 4.3 case文
case variable
when "条件1"
  puts "条件1に一致"
when "条件2"
  puts "条件2に一致"
else
  puts "どの条件にも一致しません"
end

# 5. ループ
# 5.1 while文
counter = 0
while counter < 5
  puts counter
  counter += 1
end

# 5.2 for文
for i in 0..4
  puts i
end

# 5.3 each文
array.each do |element|
  puts element
end

# 6. メソッド
# 6.1 メソッドの定義
def greet(name)
  "こんにちは、#{name}さん！"
end

# 6.2 引数
def multiply(a, b = 2)
  a * b
end

# 6.3 戻り値
def add(a, b)
  a + b  # 最後に評価された式が暗黙的に戻り値になります
end

# 7. クラスとオブジェクト
# 7.1 クラスの定義
class Person
  # 7.2 インスタンス変数
  def initialize(name)
    @name = name
  end

  # 7.3 インスタンスメソッド
  def say_hello
    "こんにちは、私は#{@name}です。"
  end

  # 7.3 クラスメソッド
  def self.species
    "Homo sapiens"
  end
end

# 7.4 継承
class Student < Person
  def study
    "#{@name}は勉強中です。"
  end
end

# 8. モジュール
module Greeter
  def greet
    "こんにちは！"
  end
end

class Host
  include Greeter
end

# 9. 例外処理
begin
  # 例外が発生する可能性のあるコード
  1 / 0
rescue ZeroDivisionError => e
  puts "エラーが発生しました: #{e.message}"
ensure
  puts "この部分は常に実行されます"
end

# 10. ブロックとProc
# ブロック
[1, 2, 3].each { |num| puts num }

# Proc
double = Proc.new { |x| x * 2 }
puts double.call(5)

# 11. ファイル入出力
File.open("example.txt", "w") do |file|
  file.write("これはファイルに書き込まれたテキストです。")
end

content = File.read("example.txt")
puts content