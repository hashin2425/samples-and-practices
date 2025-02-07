=begin
文字列型の変数は、ダブルクオーテーション・シングルクォーテーションどちらでも問題ない
基本的にはクオートで囲むやり方で大丈夫
細かく見ると、Stringクラスで生成されたインスタンスである
=end
greeting1 = "Hello11"
greeting2 = String.new("Hello22")

puts greeting1
puts greeting2

# pメソッドは、putsメソッドと違い、引数をそのまま出力する
# Print関数は、引数をそのまま出力するが、改行はされない

puts "\n"
p greeting1, greeting2
puts greeting1, greeting2
print greeting1, greeting2

=begin
    Hello11
    Hello22

    "Hello11"
    "Hello22"
    Hello11
    Hello22
    Hello11Hello22
=end

# F文字列みたいなやつは、こうやる
username = "hoge"
puts
puts(%Q[こんにちは、"#{username}"さん])

# 複数行のやつ
message = <<"EOS"
こんにちは
　こんにちは
　　こんにちは
EOS
puts message

# 文字列は、+演算子や*演算子でPythonと同じように結合や繰り返しができる
puts "Hello" + "World"
puts "Hello" * 3

# Python同様、上記のコードでは新しい文字列インスタンスが生成されるが、そうしたくない場合は、<<演算子を使う
# ただし、この場合は、元の文字列が変更されるので注意
greeting = "Hello"
greeting << "World"

#もしくは
greeging = "greeging".concat("World")
puts greeting