# Import Packages
import argparse
import sys

# Prints Fizz, Buzz, FizzBuzz divisible by 3 and 5 and both
def fizzbuzzRange(argv):
    parser = argparse.ArgumentParser(add_help=False, description=('Download reviews from BookMyShow'))
    parser.add_argument('--help', '-h', action='help', default=argparse.SUPPRESS, help='Show this help message and exit')
    parser.add_argument('--range', '-r', help='Enter range to print the Fizz, Buzz, FizzBuzz')
    args = parser.parse_args(argv)

    # Python program to print Fizz Buzz, loop for 50 times i.e. range
    for fizzbuzz in range(int(args.range)):

        # number divisible by 15 (divisible by both 3 & 5), print 'FizzBuzz' in place of the number
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print('FizzBuzz')
            continue

        # number divisible by 3, print 'Fizz' in place of the number
        elif fizzbuzz % 3 == 0:
            print('Fizz')
            continue

        # number divisible by 5, print 'Buzz' in place of the number
        elif fizzbuzz % 5 == 0:
            print('Buzz')
            continue

        # print numbers
        print(fizzbuzz)

if __name__ == '__main__':
    identifer = fizzbuzzRange(sys.argv[1:])
