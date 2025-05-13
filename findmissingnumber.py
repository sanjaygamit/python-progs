# Find missing number in an array(using summation and XOR operation)
x = [1, 2, 3, 5, 6, 7]

def get_missing_number(a):
    n = a[-1]
    sum1=0
    total1 = n*(n+1)//2
    sum1=sum(a)
    print(total1 - sum1)

def get_missing_xor(a):
    n = len(a)
    xor_a = a[0]
    for index in range(1,n):
        xor_a = xor_a ^a[index]
    x2=0
    for i in range(1,n+2):
        x2=x2^index
    print(xor_a^x2)    

get_missing_number(x)
get_missing_xor(x)      




