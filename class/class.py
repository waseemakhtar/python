class Person:
  # __init__ method is default method which gets called when the class is 
  # invoked
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Caller:
  def run(self):
    p1 = Person("John", 36)
    print(p1.name)
    print(p1.age)

# C is an 'object' derived from a class 
C = Caller()

# Call a 'run' method within an object
C.run()
