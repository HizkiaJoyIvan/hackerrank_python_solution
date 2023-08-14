if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    students = sorted(students, key = lambda x:x[1])
    scores = list(x[1] for x in students)
    lowest = scores[0]
    secondLowest = scores[0]
    i = 0
    while(i<len(scores)):
        if(scores[i]>lowest): 
            secondLowest = scores[i]
            break
        i = i + 1
    result = []
    for s in students: 
        if(s[1] == secondLowest): result.append(s[0])
    print("\n".join(sorted(result)))