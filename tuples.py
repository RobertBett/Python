my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

def making_tupes(my_dict):
    the_list = []
    # here, k and v will parse each tuple of key,value pairs returned by .iteritems()
    for k, v in the_dict.iteritems():
        the_list.append((k,v))
    return the_list