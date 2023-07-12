# 주어진 동전 n개 중에 가짜 동전(fake)을 찾아내는 알고리즘
# 입력: 전체 동전 위치의 시작과 끝(0, n-1)
# 출력: 가짜 동전의 위치 번호

def weight(a, b, c, d):
    fake = 29
    if a <= fake <= b:
        return -1
    if c <= fake <= d:
        return 1

    return 0


def find_fakecoin(left, right):
    for i in range(left + 1, right + 1):
        result = weight(left, left, i, i)
        if result == -1:
            return left
        elif result == 1:
            return i

    return -1


n = 100
print(find_fakecoin(0, n - 1))
