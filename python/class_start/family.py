class family:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_hello()

    def say_hello(self):
        print("I am {} and {} years old.".format(self.name, self.age))

class worker(family):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job
        print("I am in {}.".format(self.job))

class nonworker(family):
    def __init__(self, name, age, hobby):
        super().__init__(name, age)
        self.hobby = hobby
        print("My hobby is {}.".format(self.hobby))
