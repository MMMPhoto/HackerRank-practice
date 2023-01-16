from itertools import combinations

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
l = input()
k = int(input())

l = l.replace(' ', '')

combos = combinations(l, k)
hasA = 0
for combo in combos:
    if 'a' in combo:
        hasA += 1
prob = hasA / len(combos)
print(prob)   
