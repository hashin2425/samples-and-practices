class Person
    def say(message)
        puts message
    end

    def walk
        say("walk")
    end
end

class Athlete < Person
    def walk
        super # call the parent method
        say("I'm walking faster")
    end

    def running
        say("I'm running")
    end
end

athlete = Athlete.new()
athlete.walk()
athlete.running()
