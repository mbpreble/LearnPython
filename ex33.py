numbers = []

def append(maxNum, increment):
    for i in range (0, maxNum + 1):
        print "At the top i is %d" % i
        numbers.append(i)
    
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    

maxNum = 12
increment = 2

append(maxNum, 2)

print "The numbers: "

for num in numbers:
    print num
