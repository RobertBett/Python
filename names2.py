students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def names(arr):
 	for thing in students:
 	 print thing['first_name'], thing['last_name']
names(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
def get(arr):
	for role in users:
	 print role
	 counter=0
	 for name in users[role]:
	  # print name.values()
	  counter+=1
	  # print counter
	  first_name= name['first_name']
	  last_name= name['last_name']
	  length= len(first_name)+len (last_name)
	  # print length
	  print "{} - {} {} - {}".format(counter, first_name, last_name, length){}
get(users)