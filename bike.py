class bike(object):
 def __init__(self, price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
 def displayinfo(self):
    print 'Price is: $' + str(self.price)
    print 'Max speed: ' + str(self.max_speed) + 'mph'
    print 'Total miles: ' + str(self.miles) + ' miles'

 def ride(self):
    print 'riding'
    self.miles+=10
 def reverse(self):
    print 'reversing'
    if self.miles<=5:
       self.miles -=5
Bike = bike(100,10)
print Bike.displayinfo()
print Bike.ride()
print Bike.reverse()
