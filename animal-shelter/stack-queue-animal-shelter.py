class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name
        self.timestamp = 0


class AnimalShelter:
    def __init__(self):
        self.animal_queue = []
        self.timestamp = 0

    def enqueue(self, animal):
        animal.timestamp = self.timestamp
        self.timestamp += 1
        self.animal_queue.append(animal)

    def dequeue(self, pref):
        if pref == 'dog':
            for animal in self.animal_queue:
                if animal.species == 'dog':
                    self.animal_queue.remove(animal)
                    return animal
        elif pref == 'cat':
            for animal in self.animal_queue:
                if animal.species == 'cat':
                    self.animal_queue.remove(animal)
                    return animal
        elif self.animal_queue:
            return self.animal_queue.pop(0)

        return None

if __name__=="__main__":
    shelter = AnimalShelter()

    shelter.enqueue(Animal('dog', 'Patron')) # MY BOY
    shelter.enqueue(Animal('cat', 'Absi'))
    shelter.enqueue(Animal('dog', 'Sultan')) # MY Second BOY

    dog = shelter.dequeue('dog')
    print(dog.species, dog.name)  
    cat = shelter.dequeue('cat')
    print(cat.species, cat.name)  

    animal = shelter.dequeue('')
    print(animal.species, animal.name) 
