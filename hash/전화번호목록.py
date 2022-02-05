'''phone_book = ["119", "97674223", "1195524421"]

def solution(phone_book):
    prefix = {}
    phone_book.sort()

    pre = phone_book[0]

    for pNum in phone_book:
        if pNum.startswith(pre):
            prefix[pre] = prefix.get(pre, -1) + 1

    if(prefix[pre] != 0):
        answer = False
    else:
        answer = True

    return answer

print(solution(phone_book))'''

# 첫 제출 실패 -> sort를 하면 가장 짧은 길이의 숫자가 pre로 될 것으로 예상하고 작성한 코드였지만,
# 11, 22, 33, 123, 33123 .... -> 이런 경우에는 true를 반환하기 때문에 틀린 것으로 보인다.
# 길이가 가장 짧은 것들에 대해 dictionary를 생성하고, 그것들에 대해 startswith로 숫자를 채워주면 될듯?
# 먼저 길이가 가장 짧은 것들에 대해 dic를 생성하는 방법을 알아내야 한다.
'''
phone_book = ["119", "97674223", "1195524421", "181", "18193931", "1813917384", "998", "10"]

def solution(phone_book):
    prefix = {}
    phone_book.sort(key = len)
    shortestLen = len(phone_book[0])

    for pNum in phone_book:

        if len(pNum) == shortestLen:
            prefix[pNum] = prefix.get(pNum, -1)
        else:
            break

    # print(prefix)

    for pNum in phone_book:

        for pre in prefix:

            if pNum.startswith(pre):
                prefix[pre] += 1
            
    # print(prefix)
    print(prefix)
    numOfPrefix = sum(prefix.values())
    # 겹치는게 있으면 numOfPrefix가 0이 아닌 값. 없으면 0

    # print(numOfPrefix)

    if (numOfPrefix == 0): # 겹치는게 없으면
        answer = True
    
    else:
        answer = False


    return answer

print(solution(phone_book))'''

# 효율성 테스트 두 개와 테스트 케이스 두 개를 통과하지 못했다.... 블로그를 찾아보면...?
# 테스트 케이스를 통과하지 못한 이유를 알아냈다. ["119", "97674223", "1195524421", "181", "18193931", "1813917384", "998", "10"]
# 이런 식으로 주어지면 True를 반환해버리는 코드를 짰던 것이다.

phone_book = ["119", "97674223", "1195524421", "181", "18193931", "1813917384", "998", "1192183782748932"]

# print(sorted(phone_book)) # 문자열이라서 sort를 쓰면 119 - 1195...- 이렇게 정렬된다.
print(list(zip(sorted(phone_book), sorted(phone_book[1:]))))

def solution(phone_book):
    phone_book = sorted(phone_book)

    for pNum1, pNum2 in zip(phone_book, phone_book[1:]):
        if pNum2.startswith(pNum1):
            return False
    
    
    return True

print(solution(phone_book))

# 위의 코드는 딱히 hash를 사용하지 않은 느낌이라 hash를 사용해서 다시 작성하였다. 물론 블로그를 참고해서...


'''phone_book = ["119", "97674223", "1195524421", "181", "18193931", "1813917384", "998", "1192183782748932"]

def solution(phone_book):
    
    answer = True
    prefix_hash = {}

    for phone_number in phone_book:
        prefix_hash[phone_number] = 1

    for phone_number in phone_book:
        temp = ""

        for digit in phone_number:
            temp += digit
            
            if temp in prefix_hash and temp != phone_number:
                answer = False
                return answer

    return answer

'''
