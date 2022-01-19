from functools import reduce
# clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
def solution(clothes):

    answer = 0
    matches = {}
    mul = 1

    for c in clothes:
        
        matches[c[1]] = matches.get(c[1], 1) + 1

    # print(matches)
    # print(len(matches))
    # print(clothes[0][1])

    answer = reduce(lambda x, y: x*y, matches.values()) - 1

    return answer

# print(solution(clothes))