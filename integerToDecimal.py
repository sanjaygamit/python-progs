# Converting an Integer into Decimal

import decimal
integer = 111
print(decimal.Decimal(integer))
print(type(decimal.Decimal(integer)))

# Converting an String of Integers into Decimals 

string = '12345'
a = decimal.Decimal(string)
print(a)
print(type(a))