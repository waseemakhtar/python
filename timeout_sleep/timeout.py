#Executes in both python/python3
'''
Decrement a given number every 1 second until it reaches 0
'''

from time import sleep
import sys
#import time

def print_num():
    'Takes input from command line and converts the string to int'
    n = int(sys.argv[1])
    while n > 0:
        print(n)
        sleep(1)
#       time.sleep(1)
        n = n - 1

print_num()
