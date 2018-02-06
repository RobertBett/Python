import random
def grades(rps):
  print "Score and Grades"
  for x in range(0, rps):
   x= random.randint(60,101)
   if x>=60 and x<=70:
    print "Score:",x,"your grade is D"
   elif x>=70 and x<=80:
    print "Score:",x,"your grade is C"
   elif x>=80 and x<=90:
    print "Score:",x,"your grade is B"
   elif x>=90 and x<=100:
    print "Score:",x,"your grade is A"
   else:
	print"you Failed"
grades(1)
print "end of the program Bye!"
	  