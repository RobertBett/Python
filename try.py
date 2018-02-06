x = [2,54,-2,7,12,98]
print max(x)
print min(x)
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[-1]
y=[]
y.append(0)
y.append(-1)
#
words = "It's thanksgiving day. It's my birthday,too!"
print words.find('day')
print words.replace('day','month')


r=[]
# for val in "hello":
#   if  == "o":
#     # break
#    r.append(0)
# v=0
# for val in word_list [v]:
#  	 while val == "o":
#  		print word_list[2]
#  		v+=1
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print x
first_list = x[:len(x)/2] # optional first parameter of slice defaults to zero
second_list = x[len(x)/2:] # optional second parameter of slice defaults to the list's length
print "first list", first_list
print "second_list", second_list
second_list.insert(0,first_list)
print second_list




