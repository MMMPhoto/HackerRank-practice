n = int(input())
arr = map(int, input().split())
allScores = list(arr)

firstPlace = max(allScores)
remainingScores = [i for i in allScores if i != firstPlace]

secondPlace = max(remainingScores)
print(firstPlace)
