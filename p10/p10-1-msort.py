# 쉽게 설명한 병합 알고리즘
# 입력: 리스트 a
# 출력: 정렬된 새 리스트

def merge_sort(a):
    n = len(a)

    if n <= 1:
        return a

    mid = n // 2
    g1 = merge_sort(a[:mid])
    g2 = merge_sort(a[mid:])

    result = []

    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))

    while g1:
        result.append(g1.pop(0))

    while g2:
        result.append(g2.pop(0))

    return result


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(merge_sort(d))
