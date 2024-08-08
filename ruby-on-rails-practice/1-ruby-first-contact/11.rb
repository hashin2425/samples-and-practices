class Car
    @speed = 90
    @@car_count = 0

    def initialize(name)
        @name = name
        @@car_count += 1
    end

    def say_name
        puts @name
    end
    # private :say_name # private method

    def run
        puts "Speed: #{@speed}"
    end

    def get_car_count
        puts @@car_count
    end
end

car = Car.new("Ferrari")
car2 = Car.new("Lamborghini")
car.get_car_count()
car.run()
car.say_name()
car::say_name() # 同じ

class Person
    def initialize(name)
        @name = name
    end
    attr_accessor :name
end

class SecurePerson
    def initialize(name)
        @name = name
    end
end


person1 = Person.new("Alice")
person2 = SecurePerson.new("Bob")
person1.name = "Alice!!"
# person2.name = "Bob!!" # undefined method
puts person1.name
# puts person2.name # undefined method

