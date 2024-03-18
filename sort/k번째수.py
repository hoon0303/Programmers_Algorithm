def solution(array, commands):
    answer = []
    
    for command in commands:
        i = command[0] - 1
        j = command[1]
        k = command[2] - 1
        
        x = array[i:j]
        x.sort()
        answer.append(x[k])
    return answer