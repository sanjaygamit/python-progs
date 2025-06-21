# Converting an Integer into Decimal

# import decimal
# integer = 111
# print(decimal.Decimal(integer))
# print(type(decimal.Decimal(integer)))

# Converting an String of Integers into Decimals 

# string = '12345'
# a = decimal.Decimal(string)
# print(a)
# print(type(a))

# Reversing a String using an Extended Slicing Technique. 

# string = 'Python programming'
# a = string[::-1]
# print(a)

# Counting VOWELS  in a given word 
# vowel = ['a','e','i','o','u']
# word = "programming"
# count = 0 
# for i in word:
#     if i  in vowel: 
#         count +=1
# print(count) 

# Counting CONSONANTS  in a given word. 
# vowel = ['a','e','i','o','u']
# word = "programming"
# count = 0 
# for i  in word:
#     if i not in vowel: 
#         count +=1
# print(count) 

# Counting the number of occurances of a character in a string 
# word = "programming"
# character = 'g'
# count = 0 
# for I in word: 
#     if I == character: 
#         count +=1
# print(count)        

# Writing FIBONACCI Series 
# fib = [0,1]
# Range starts from 0 by default 
# n = 10 
# for i in range(n):
#     fib.append(fib[-1] + fib[-2])
# Converting the list of integers to string 
# print(','.join(str(e) for e in fib))
# print(fib)

# Finding the Maximum Number in a list 
# numberList = [12,3,55,23,6,78,33,4,407]
# max = numberList[0]
# min = numberList[0]
# for i in numberList: 
#     if max < i:
#         max = i
#     elif min > i:
#         min = i
# print(max,min)        


# numberList = [12,3,55,23,6,78,33,4]
# min = numberList[0]
# for i in numberList:
#     # print(i)
#     if min > i:
#         min = i
# print(min)        

# Finding the middle Element in a List 
# numList = [12,3,55,23,6,78,33,4]
# midElement = int((len(numList)/2))
# print(midElement)
# print(f"Middle Element is : {numList[midElement]}")

# Converting a list into a string. 
# list = ["P","Y","T","H","O","N"]
# string = "".join(list)
# print(string)

# Adding Two List Element Together 
# list1 = [1,2,3]
# list2 = [4,5,6]
# res_lst = []
# for i in range(0,len(list1)):
#     print(i)
#     res_lst.append(list1[i] + list2[i])
# print(res_lst)   

# Comparing Two Strings for ANAGRAMS 

# str1 = "listen"
# str2 = "silent"
# str1 = str1.lower()
# str2 = str2.lower()

# if sorted(str1) == sorted(str2):
#     print("Anagrams")
# else: 
#     print("Not Anagrams")    

# Checking for PALINDROME using Extended slicing technique. 

# str1 = "Kayak".lower()
# if str1 == str1[::-1]:
#     print("palindrome")
# else: 
#     print("Not Palindrome")       


## Counting the white spaces in a string. 
string = "p r ogram in g"
print(string.count(" "))