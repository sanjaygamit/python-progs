# Write a python program to count the frequency of words appearing in a string. 

# eg: Sheena loves eating apple and mango. Her sister also loves eating apple and mango, loves loves loves. 

# def word_frequency():
#     str = input("Enter a string: ")
#     li = str.split()
#     # print(li)
#     d = {}
#     for i in li:
#         # print("List value",i)
#         if i not in d.keys():
#             d[i] = 0
#         # print("dictionary value",d[i])    
#         d[i]=d[i]+1 
#     print(d) 

# word_frequency()          





# I my name is Sanjay, I am 38 and I am a Software Engineer. I am from India. I love coding and I love Python.

# def word_frequency():
#     str = input("Enter a string : ")
#     li = str.split()
#     d = {}
#     for  i in li:
#         if i not in d.keys():
#             d[i] = 0
#         d[i] = d[i] + 1
#     print(d)
# if __name__ == "__main__":
#     word_frequency()            

# Write a python program to convert two lists into a dictionary. 

def fn_to_dict():
    key = [1,2,3]
    value = ["one", "two", "three"]
    result = dict(zip(key,value))
    print(result)


fn_to_dict()    

