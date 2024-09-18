from itertools import permutations

# 소수 판별 함수
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    possible_numbers = set()  # 가능한 숫자를 담을 집합 (중복 제거)
    
    # 숫자로 만들 수 있는 모든 순열 생성 (1자리부터 len(numbers)자리까지)
    for length in range(1, len(numbers) + 1):
        for perm in permutations(numbers, length):
            num = int(''.join(perm))  # 순열을 정수로 변환
            possible_numbers.add(num)
    
    # 소수인 숫자들을 찾아 개수 카운트
    prime_count = sum(1 for num in possible_numbers if is_prime(num))
    
    return prime_count