# def checkerboard():
#  for i in range(0, 8):
#         if i%2 == 0:
#             print "* " * 4
#         else:
#             print " *" * 4
# checkerboard()
def add(a,b):
  x = a - b
  return x
# the return value gets assigned to the "result" variable
result = add(5,3)
print result # this should print 8
# invoking the function passing in one argument
# this function has one parameter(input)
def say_hi(name):
  print "Hi, " + name
say_hi('Michael')
say_hi('Anna')
say_hi('Eli')

def addd(a,b):
  x = a + b
  return x
sum1 = addd(4,6)
sum2 = addd(1,4)
sum3 = sum1 + sum2
print sum3
print sum2
print sum1

def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b

