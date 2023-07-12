# 최대값의 위치 구하기
# 입력: 숫자가 n개 들어있는 리스트
# 출력: 숫자 n개 중에서 최대값이 있는 위치(0부터 n-1개까지의 값)


def find_max_index(a):
    max_index = 0

    for i in range(1, len(a)):
        if a[max_index] < a[i]:
            max_index = i

    return max_index


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max_index(v))
