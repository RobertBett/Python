info = [
 {'id':'My name is','in': ' Anna'},
 {'id':'My age is','in':' 101'},
 {'id':'My country of birth is','in':' The United States'},
 {'id':'My favorite language is','in': ' Python' }
]
def bio(arr):
 for thig in info:
    thing= thig['id']+ thig['in']
    print thing
bio(info)