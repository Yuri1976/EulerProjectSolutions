n1, n2 = 0,1
count = 0
nterms = int(input("How many terms? "))
fibList = []
sumList = []

while count < nterms:
    fibList.append(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
    
for n in fibList:
    if n%2 == 0 and n < 4000000:
        sumList.append(n)
        
sum(sumList)