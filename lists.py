def practice():
	 words = ("It's thanksgiving day. It's my birthday,too!")
	 new_words= words.replace('day','month')
	 print new_words
practice()
def nums():
	x = [2,54,-2,7,12,98]
	x.sort()
	num = x
	print num
nums()
def odds():
 	for odd in range(0,200):
		if odd % 2==0:
		 print "number is",odd,"this is an odd number" 
		else:
		 print "number is ",odd ,"this is an even number"
 
odds()