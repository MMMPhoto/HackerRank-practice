    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    allMarks = student_marks[query_name]
    average = sum(allMarks) / 3
    
    floatAverage = "{:.2f}".format(average)
    print(floatAverage)
