 # Write a program that outputs “even” if a number is even and “odd” if a number is odd.
# Think about what if the value is neither even nor odd (the value can be fractional or it can even not be a number at all).


int_num = int(input('Enter number: ' ))

if int_num % 2 ==0:
    print(int_num, 'is EVEN')
else:
    print(int_num, 'IS ODD')
