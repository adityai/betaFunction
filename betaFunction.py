# Author: Aditya Inapurapu

import math

# Function to calculate Euler's beta function
def beta(p, q):
    return float(math.factorial(p - 1)) * float(math.factorial(q - 1)) / float(math.factorial(p + q - 1))

def main():
    print('Beta function results for p = 1 to 9 and q = 1 to 9:')
    for i in range(1, 10, 1):
        for j in range(1, 10, 1):
            print( 'beta(' + str( i ) + ', ' + str( j ) + ') = ' + str( beta( int( i ), int( j ) ) ) )

    print('Calculate beta(p, q) = p! x q! / (p + q - 1)!')
    p = int(input('p = '))
    q = int(input('q = '))
    print(beta(p, q))

main()
