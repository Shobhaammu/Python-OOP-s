class Animal:
    def speak(self):
        return "Animal makes a sound Moo"
    
class Dog(Animal):
    def speak(self):
        return "woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
class Cow(Animal):
    #def speak(self):
     #   return "Moo!"
     pass
    
def make_animal_speak(animal):
    print(animal.speak())
    
dog=Dog()
cat=Cat()
cow=Cow()

print("Dog says:",dog.speak())
print("cat says:",cat.speak())
print("cow says:",cow.speak())

#make_animal_speak(dog)
#make_animal_speak(cat)
#make_animal_speak(cow)

