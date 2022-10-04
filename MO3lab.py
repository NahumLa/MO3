#Superclass Vehicle
class Vehicle():
    def __init__(self, vehicle_type):
        self.type = type
 
#Subclass Automobile(from Vehicle)  
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

#Get user information about vehicle        
type = input("What type of vehicle is it?")
year = input("What year is the vehicle?")
make = input("What is the make?")
model = input("What is the model?")
doors = input("How many doors does it have?")
roof = input("Solid or sunroof?")

#Make car object
car1 = Automobile(type, year, make, model, doors, roof)    

#Print vehicle details
print("Vehicle details:")
print("Vehicle type: " + car1.type)
print("Vehicle year: " + car1.year)
print("Vehicle make: " + car1.make)
print("Vehicle model: " + car1.model)
print("Number of doors: " + car1.doors)
print("Roof type: " + car1.roof)