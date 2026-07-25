# Implement the Person class
# code here

class Person:
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age
    
    def __init__(self):
        self.name = 'Geeks'
        self.age = 10 
    
