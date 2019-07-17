class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
p1=Person("Elvis",36)
print(p1.name)
print(p1.age)

def speak():
    print("hello")
def walk():
    print("walking away")
def get_name():
    name1=input("enter your name")
    print(name1)
speak()
walk()
get_name()
