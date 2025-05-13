# Write a python program to count the frequency of words appearing in a string. 

# eg: Sheena loves eating apple and mango. Her sister also loves eating apple and mango, loves loves loves. 

def word_frequency():
    str = input("Enter a string: ")
    li = str.split()
    # print(li)
    d = {}
    for i in li:
        # print("List value",i)
        if i not in d.keys():
            d[i] = 0
        # print("dictionary value",d[i])    
        d[i]=d[i]+1 
    print(d) 

word_frequency()          