# Write a python program to convert two lists into a dictionary. 

def list_to_dict():
    keys = [1,2,3]
    values = ["one", "two", "three"]
    result = dict(zip(keys,values))
    print(result)

def dict_to_touple():
    x = {1: "one", 2: "two", 3: "three"}
    #result = tuple(x.items())
    for i in x.items():
        print(i)



list_to_dict()
dict_to_touple()
