# 쉽게 설명한 선택정렬
# 입력: 리스트 a
# 출력: 정렬된 새리스트
# 주어진 리스트에서 최소값의 위치를 돌려주는 함수

def find_min_index(a):
    n = len(a)
    min_index = 0

    for i in range(1, n):
        if a[min_index] > a[i]:
            min_index = i

    return min_index


def sel_sort(a):
    result = []

    while a:
        min_index = find_min_index(a)
        value = a.pop(min_index)
        result.append(value)

    return result


d = [2, 4, 5, 1, 3]
print(sel_sort(d))
