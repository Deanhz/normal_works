# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 10:53:58 2018

@author: Dean
"""

class Pet(object):
    def __init__(self,type):
        self.type = type
    def getPetType(self):
        return self.type

class Dog(Pet):
    def __init__(self):
        super().__init__("dog")

class Cat(Pet):
    def __init__(self):
        super().__init__("cat")

class PetEnterQueue(object):
    def __init__(self,pet,count):
        self.pet = pet
        self.count = count
    def getPet(self):
        return self.pet
    def getCount(self):
        return self.count
    def getEnterPetType(self):
        return self.pet.getPetType()

class DogCatQueue(object):
    def __init__(self):
        self.dogQ = []
        self.catQ = []
        self.count = 0
    def add(self, pet):
        if pet.getPetType() == "dog":
            self.dogQ.append(PetEnterQueue(pet,self.count+1))
        elif pet.getPetType() == "cat":
            self.catQ.append(PetEnterQueue(pet,self.count+1))
        else:
            raise Exception("Err,not dog or cat")
    def pollAll(self):
        if self.dogQ and self.catQ:
            if self.dogQ[-1].getCount() <self.catQ[-1].getCount():
                return self.dogQ.pop().getPet()
            else:
                return self.catQ.pop().getPet()
        elif self.dogQ:
            return self.dogQ.pop().getPet()
        elif self.catQ:
            return self.catQ.pop().getPet()
        else:
            raise Exception("Err, queue is empty")
            
    def pollDog(self):
        if self.dogQ:
            return self.dogQ.pop().getPet()
        else:
            raise Exception("Dog queue is empty")
    def pollCat(self):
        if self.catQ:
            return self.catQ.pop().getPet()
        else:
            raise Exception("Cat queue is empty")
    
    def isEmpty(self):
        if not self.catQ and not self.dogQ:
            return True
        else:
            return False
    
    def isDogQueueEmpty(self):
        return not self.dogQ
    
    def isCatQueueEmpty(self):
        return not self.catQ




if __name__ == "__main__":
    d = Dog()
    c = Cat()
    Q = DogCatQueue()
    Q.add(d)
    Q.add(d)
    Q.add(c)
    Q.add(c)
    print(Q.pollAll().getPetType())
    
    