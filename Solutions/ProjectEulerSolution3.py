import math

number = 600851475143
primeNumbers = []

#starting with even
while number%2 == 0:
    primeNumbers.append(2)
    number = number/2

#now it must be odd
for i in range(3,int(math.sqrt(number))+1, 2):
    while number%i == 0:
        primeNumbers.append(i)
        number = number/i

print(primeNumbers)
max(primeNumbers)