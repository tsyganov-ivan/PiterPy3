class Rule
    attr_accessor :attribute
    attr_accessor :value

    def initialize(&block)
        instance_eval &block
    end

    def process(filepath)
        puts 'Update '+filepath
        puts '   '+@attribute+' = '+@value
    end

    def method_missing name, *args, &block
        @attribute=name.to_s
        @value=args[0]
    end
end

class Task
    def initialize &block
        @rules = Array.new
        instance_eval &block
    end

    def with value
        @with=value
    end

    def inside value
        @inside=value
    end

    def rule &block
        @rules << Rule.new(&block)
    end

    def run
        puts 'Work dir: '+@inside
        puts 'Mask: '+@with
        files = ['test.mp3', 'new.mp3']
        for file in files
            for rule in @rules
                rule.process(file)
            end
        end
    end
end

task = Task.new do
    with '*.\.mp3'
    inside './music'
    rule do
        Artist 'Metallica'
    end
    rule do
        Genge 'Rock'
    end
end
task.run()
