from helper import upCap

class Waiter:
    waiters = []
    def __init__(self, name : str, age : int, gender : str):
        self.name, self.gender = upCap(name, gender)
        self.age = age

        Waiter.waiters.append(self)

    def __str__(self):
        return f"Name : {self.name} | Age : {self.age} | Gender : {self.gender}"

class Chef:
    chefs = []
    def __init__(self, name : str, age : int, gender : str):
        self.name = upCap(name)
        self.age = age
        self.gender = gender

        Chef.chefs.append(self)
        
    def __str__(self):
        return f"Name : {self.name} | Age : {self.age} | Gender : {self.gender}"

class Manager:
    managers = []
    def __init__(self, name : str, age : int, gender : str, isMarried : bool):
        name, gender = upCap(name, gender)
        if gender == 'Female':
            if isMarried:
                self.name = 'Mrs ' + name
            else:
                self.name = 'Miss ' + name 
        else:
            self.name = 'Mr ' + name   
        
        self.age = age
        self.gender = gender
        self.isMarried = isMarried

        Manager.managers.append(self)
        
    def __str__(self):
        return f"Name : {self.name} | Age : {self.age} | Gender : {self.gender} | Married : {self.isMarried}"

class Cleaner:
    cleaners = []
    def __init__(self, name : str, age : int, gender : str):
        self.name, self.gender = upCap(name, gender)
        self.age = age

        Cleaner.cleaners.append(self)
        
    def __str__(self):
        return f"Name : {self.name} | Age : {self.age} | Gender : {self.gender}"

if __name__ == '__main__':
    print("This file is supposed to be used as imported module.")
    exit()