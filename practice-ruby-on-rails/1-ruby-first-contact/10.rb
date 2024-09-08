def greeting(name="default_name")
    puts "Hello, #{name}!"
end

greeting("Alice") # => "Hello, Alice!"
greeting # => "Hello, default_name!"

def groups(*names)
    names.each{|name|
        print name
        print ", " if name != names.last
    }
    puts ""
end

groups("Alice", "Bob", "Charlie") # => "AliceBobCharlie"

def caluc(a,b)
    return a - b, a + b
end

result1, result2 = caluc(10, 5)
puts result1 # => 5
puts result2 # => 15