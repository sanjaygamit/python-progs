# Write a Python program to find out common letters between two strings. 
# eg :- 3
#    sanjay , beaula 
# & for extarcting common letters from two strings


def common_letters():
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")

    # Convert both strings to sets to find common letters
    set1 = set(str1)
    set2 = set(str2)
    
    # Find common letters
    common = set1 & set2
    print("Common letters:", common) 

common_letters()


