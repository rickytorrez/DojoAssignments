class Product:

    def __init__ (self,price,item_name,weight,brand):

        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sellStatus(self):
        self.status = "sold"
        # print("The", self.item_name, "has been 'sold'")
        return self 

    def addTax(self, tax):
        self.tax = tax
        print self.tax
        self.tax = self.price * self.tax
        print(self.price + self.tax)
        return self

    def sellStatus(self, reason):                       ## sellStatus takes a parameter of reasons why the product is being returned ##
        self.reason = reason
        if self.reason == "Defective":
            self.status = "Defective"
            self.price = 0
            print self.status,",", self.price
        elif self.reason == "In the box":
            self.status = "for sale"
            print self.status
        elif self.reason == "open box":
            self.status = "used"
            self.price = self.price*0.8
            print self.price
        else:
            print("Invalid")
        return self

    def displayInfo(self):
        print 'Item Name:', self.item_name
        print 'Price:','$',self.price
        print 'Weight:', self.weight
        print 'Brand:', self.brand
        print 'Status:', 'The item is', self.status
        return self


my_product=Product(10,'apple',1,'arizona') 
print my_product.displayInfo()
# my_product.addTax(.05)
# my_product.sellStatus("open box")
