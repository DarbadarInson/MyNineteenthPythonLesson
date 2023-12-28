import random

class Human():
   
  def __init__(self,name: str,age: int): #this is a special method
    self.name = name
    self.age = age

  def eat(self): #this is a method

    food = ['burger','spaghetti','orange','broccoli'] 
    print(f"{self.name.title()} ate a {random.choice(food)}")

  def birthday(self): #this is a method
    
    self.age += 1
    print(f"It's your birthday {self.name.title()} you are now {self.age} years old!")

  def sleep(self): #this is a method
      
      hours = [6,7,8]
      print(f"{self.name.title()} you went to sleep and slept for {random.choice(hours)} hours!")


human1 = Human("Joe", 5) #this is an instance of the class Human
print(f"Name : {human1.name}")
print(f"Age : {human1.age}")
human1.eat()
human1.birthday()
print(f"Age : {human1.age}")
human1.sleep()

