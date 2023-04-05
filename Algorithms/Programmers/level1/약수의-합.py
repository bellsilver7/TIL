def solution1(n):
    if n == 0:
        return 0

    tmp = []
    for i in range(1, n + 1):
        if n % i == 0:
            tmp.append(i)
    
    answer = sum(tmp)
    return answer


def solution2(n):
    if n == 0:
        return 0

    tmp = [i for i in range(1, (n // 2) + 1) if n % i == 0]
    
    answer = n + sum(tmp)
    return answer