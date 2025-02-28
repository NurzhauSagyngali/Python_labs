import math
import time

number = int(input())
milliseconds = int(input())

time.sleep(milliseconds / 1000) # stops 

print(f"Square root of {number} after {milliseconds} milliseconds is {math.sqrt(number)}")