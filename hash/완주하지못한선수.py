participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]


def solution(participant, completion):
    temp = {}
    answer = ''
    
    for i in participant:
        temp[i] = temp.get(i, 0) +1
    
    for j in completion:
        temp[j] = temp.get(j) - 1

    for t in temp:
        if temp[t] == 1:
            answer = t
        
    return answer

print(solution(participant, completion))
