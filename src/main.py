'''
Created on Sep 7, 2017

@author: jlearx
'''

if __name__ == '__main__':
    divisors = []
    
    number = int(input("Please enter a number: "))
    
    print("Listing all divisors (factors) of " + str(number) + ":")
    
    divisors = [n for n in range(1, number + 1) if (number % n == 0)]
    cnt = len(divisors)
    
    for i in range(0, cnt):
        if (i < (cnt - 1)):
            print(divisors[i], end=', ')
        else:
            print(divisors[i])
    