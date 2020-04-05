mylist = list(range(0,1000))
total = 0

for num in mylist:        
    
    if num%3 == 0 or num%5 == 0:
        total += num

print(total)