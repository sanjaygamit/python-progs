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


numberList = [12,3,55,23,6,78,33,4]
min = numberList[0]
for i in numberList:
    # print(i)
    if min > i:
        min = i
print(min)        