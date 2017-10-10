import math
import time

knowPrimes = [2,3]
# Even number except 2 cannot be prime 
# Any number divisible by an other prime number smaller that it cannot be a prime
# How small ?
# Sqaure root of the number
primeRange = 1000
startTime = time.time()
for number in range(5,primeRange,2):
    isprime = True
    for smallprime in knowPrimes:
        if number % smallprime == 0:
            isprime = False
            # print(" I am not prime number",number)
            break
        else:
            if smallprime > math.sqrt(primeRange):
                break
            else:
                pass


            # pass

    if isprime == True:
        knowPrimes.append(number)

print(knowPrimes)
print("Time taken in seconds " ,time.time()-startTime)

# print(knowPrimes)
print(len(knowPrimes))