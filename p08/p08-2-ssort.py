# 쉽게 설명한 선택정렬
# 입력: 리스트 a
# 출력: 없음(입력으로 주어진 a가 정렬됨)

def sel_sort(a):
    n = len(a)
    for i in range(0, n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if a[min_idx] > a[j]:
                min_idx = j
        a[min_idx], a[i] = a[i], a[min_idx]


d = [2, 4, 5, 1, 3]
sel_sort(d)
print(d)
