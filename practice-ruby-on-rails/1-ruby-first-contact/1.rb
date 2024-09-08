# coding: utf-8
# 文字コードも指定できたりするが、UTF-8がデフォルトなので指定しなくても良い

puts "hello world"

# セミコロンは合っても無くてもOK　リンターなどでどちらかに揃えるべきか
puts "num0"; puts "num1"; puts "num2"
puts "NUM0", "NUM1", "NUM2";
puts "howdy";
p __ENCODING__

=begin
複数行コメント
あ
あ
=end