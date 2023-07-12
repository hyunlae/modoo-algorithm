# 최대값 구하기
# 입력: 숫자가 n개 들어 있는 리스트
# 출력: 숫자 n개 중 최대값

def find_max(a):
    max_value = a[0]

    for i in range(1, len(a)):
        if a[i] > max_value:
            max_value = a[i]

    return max_value


v = [17, 92, 18, 33, 58, 7, 33, 42]

print(find_max(v))
