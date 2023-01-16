from itertools import product
# Enter your code here. Read input from STDIN. Print output to STDOUT
def func(x):
    x = x * x
    return x

lineOne = input()
lineOne = lineOne.split(' ')
k = int(lineOne[0])
m = int(lineOne[1])

listOfLists = []
for line in range(0, k):
    line = input()
    list = line.split(' ')
    list.pop(0) 
    listOfLists.append(list)

allCombos = []
for combo in product(*listOfLists):
    allCombos.append(combo)
    
biggestS = 0
for combo in allCombos:
    s = 0
    for each in combo:
        s = s + func(int(each))
    print(s)
    s = s % m
    print(s)
    if s > biggestS:
        biggestS = s   

print(biggestS)
