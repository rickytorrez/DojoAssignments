class Bike:

    def __init__ (self, price, max_speed):
        
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayInfo(self):
        print self.price
        print self.max_speed
        print self.miles
        return self

    def ride(self):
        # self.miles = self.miles + 10
        self.miles +=20
        print 'Riding'
        print 'Total miles ridden:', self.miles
        return self

    def reverse(self):
        self.miles -=5
        if self.miles <= 0:
            self.miles = 0
        print 'Reversing'
        print 'Total miles ridden:', self.miles
        return self

my_bike=Bike(1000, 50)

# print my_bike.displayInfo()
# print my_bike.ride()
# print my_bike.reverse()

my_bike.ride().ride().ride().reverse().reverse().displayInfo()

