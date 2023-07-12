# 쉽게 설명한 퀵 정렬
# 입력: 리스트a
# 출력: 정렬된 새 리스트

def quick_sort(a):
    n = len(a)

    if n <= 1:
        return a

    pivot = a[-1]
    g1 = []
    g2 = []

    for i in range(0, n - 1):
        if a[i] < pivot:
            g1.append(a[i])
        else:
            g2.append(a[i])

    return quick_sort(g1) + pivot + quick_sort(g2)
