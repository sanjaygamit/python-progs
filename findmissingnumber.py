# Find missing number in an array(using summation and XOR operation)
x = [1, 2, 3, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20]

def get_missing_number(a):
    n = a[-1]
    sum1=0
    total1 = n*(n+1)//2
    sum1=sum(a)
    print(total1 - sum1)

get_missing_number(x)    