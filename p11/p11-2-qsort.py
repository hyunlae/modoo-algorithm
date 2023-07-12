# 퀵 정렬
# 입력: 리스트 a
# 출력: 없음(입력으로부터 주어진 a가 정렬됨)
# 리스트 a에서 어디서부터 어디까지가 정렬 대상인지
# 범위를 지정하여 정렬하는 재귀 호출함수

def quick_sort_sub(a, start, end):
    if end - start <= 0:
        return

    pivot = a[end]
    i = start

    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1

    a[i], a[end] = a[end], a[i]

    quick_sort_sub(a, start, i - 1)
    quick_sort_sub(a, i + 1, end)


def quick_sort(a):
    quick_sort_sub(a, 0, len(a) - 1)


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
quick_sort(d)
print(d)