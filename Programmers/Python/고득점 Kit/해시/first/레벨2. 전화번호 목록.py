from itertools import combinations

# solution 1. startwith, zip 함수 사용
def solution(phone_book):
    phone_book = sorted(phone_book)

    for a,b in zip(phone_book,phone_book[1:]):
        if b.startswith(a):
            return False

    return True

# 리스트 슬라이싱을 활용한 방법
def solution2(phone_book):
    phone_book.sort()

    for i in range(1,len(phone_book)):
        a=phone_book[i-1]
        b=phone_book[i]
        if b[:len(a)] == a:
            return False

    return True

# 해싱 - 딕셔너리를 활용한 방법
def solution3(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp=""
        for number in phone_number:
            temp+=number
            if temp in hash_map.keys() and temp!=phone_number:
                return False


    return True



phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))
print(solution2(phone_book))
print(solution3(phone_book))