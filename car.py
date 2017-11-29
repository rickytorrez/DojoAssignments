class Car:

    def __init__ (self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price>10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

    def display_all(self):
        print 'Price:', "$",self.price
        print 'Speed:', self.speed,"mph"
        print 'Fuel:', self.fuel,
        print 'Mileage', self.mileage,"mpg"
        print 'Tax', self.tax, "%"
        return self

my_car1=Car(2000,35,"Full",15)
my_car2=Car(2000,5,"Not Full",105,)
my_car3=Car(2000,15,"Kind of Full",95)
my_car4=Car(2000,25,"Full",25)
my_car5=Car(2000,45,"Empty",25)
my_car6=Car(2000000,35,"Empty",15)

print my_car1.display_all()
print my_car2.display_all()
print my_car3.display_all()
print my_car4.display_all()
print my_car5.display_all()
print my_car6.display_all()
