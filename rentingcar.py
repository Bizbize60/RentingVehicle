class Vehicle:
    
    def __init__(self,Id,Type,numberPlate,basePrice):
        self.Id=Id
        self.Type=Type
        self.numberPlate=numberPlate
        self.basePrice=basePrice
        
        
    def calculatecost(self):
        print("just working for subclasses")
        
        
        
        
        
class Car(Vehicle):

    def __init__(self,Id,Type,numberPlate,basePrice,airbag,gearType,age):
            super().__init__(Id,Type,numberPlate,basePrice)
            self.airbag=airbag
            self.gearType=gearType
            self.age=age
            
            
    def calculatecost(self):
            self.price=0
            if self.airbag:
                self.price=self.basePrice+50
            if self.age<5:
                self.price+=50
            return self.price   
        
        
        
class Motor(Vehicle):
    def __init__(self,Id,Type,numberPlate,basePrice,motorType):
        super().__init__(Id,Type,numberPlate,basePrice)
        self.motorType=motorType
            
            
    def calculatecost(self):
        self.price=0
        if self.motorType=="scooter":
            self.price=self.basePrice+50
        if self.motorType=="motorbike":
            self.price=self.basePrice+100
            
        return self.price

class Carrier(Vehicle):
    def __init__(self,Id,Type,numberPlate,basePrice,fuelType):
        super().__init__(Id,Type,numberPlate,basePrice)
        self.fuelType=fuelType
    def calculatecost(self):
        print("just working for subclasses")
        
class Bus(Carrier):
    def __init__(self,Id,Type,numberPlate,basePrice,fuelType,seat):
        super().__init__(Id,Type,numberPlate,basePrice,fuelType)
        self.seat=seat
    def calculatecost(self):
        self.price=0
        if self.fuelType=="fueloil":
            self.price=self.basePrice+30+(10*self.seat)
        elif self.fuelType=="diesel":
            self.price=self.basePrice+40+(10*self.seat)
        return self.price        
class Truck(Carrier):
    def __init__(self,Id,Type,numberPlate,basePrice,fuelType,tonnage):
        super().__init__(Id,Type,numberPlate,basePrice,fuelType)
        self.tonnage=tonnage
    def calculatecost(self):
        self.price=0
        if self.fuelType=="fueloil":
            self.price=self.basePrice+30+(100*self.tonnage)
        elif self.fuelType=="diesel":
            self.price=self.basePrice+40+(100*self.tonnage)
        return self.price        
                
    

class Customer:
    def __init__(self,customerId,name):
        self.customerId=customerId
        self.name=name
    def rentVehicle(self,vehicle):
        if self.canRent(vehicle):
            print(f"{self.name} rented {vehicle.Type} with ID {vehicle.Id}.")
        else:
            print(f"{self.name} cannot rent  with ID {vehicle.Id}.")
    def canRent(self):
        print("just working for subclasses")
class Person(Customer):
    def __init__(self,customerId,name,drivingLicense):
        super().__init__(customerId,name)
        self.drivingLicense=drivingLicense
    def canRent(self,vehicle):
        if isinstance(vehicle,Car) and self.drivingLicense=="B":
            return True
        
        elif isinstance(vehicle,Motor) and self.drivingLicense=="A1":
            return True
        else:
            return False
class Company(Customer):
    def __init__(self,customerId,name,yearInCorporation):
        super().__init__(customerId,name)
        self.yearInCorporation=yearInCorporation
    def canRent(self,vehicle):
        if isinstance(vehicle,Carrier):
            return True
            
car1=Car(1,"Car","60bc60",200,True,"automatic",3)
print(car1.calculatecost())
person1=Person(100,"ali","B")
person1.rentVehicle(car1)