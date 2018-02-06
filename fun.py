#odd and Even 
# def odd_even():
# 	for x in range(0,2001):
# 	 if x % 2==0:
# 	   print "Number is ",x,"this is an even number"
# 	 else:
# 	  print "Number is ",x,"this is an odd number"
# odd_even()
def multiply(arr,num):
	for x in range(len(arr)):
		arr [x]*=num
	return arr
a=[2,4,10,16]
b= multiply(a,5)
print b