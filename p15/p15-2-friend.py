# 친구리스트에서 자신의 모든 치구를 찾고 친구들의 친밀도를 계산하는 알고리즘
# 입력: 친구 관계 그래프 g, 모든 친구를 찾을 자신 start
# 출력: 모든 친구의 이름과 자신과의 친밀도
from collections import deque


def print_all_friends(g, start):
    qu = deque()
    done = set()

    qu.append((start, 0))
    done.add(start)

    while qu:
        (p, d) = qu.popleft()
        print(p, d)
        for x in g[p]:
            if x not in done:
                qu.append((x, d + 1))
                done.add(x)


fr_info = {
    "Summer": ["John", "Justin", "Mike"],
    "John": ["Summer", "Justin"],
    "Justin": ["John", "Summer", "Mike", "May"],
    "Mike": ["Summer", "Justin"],
    "May": ["Justin", "Kim"],
    "Kim": ["May"],
    "Tom": ["Jerry"],
    "Jerry": ["Tom"]
}

print_all_friends(fr_info, "Summer")
print()
print_all_friends(fr_info, "Jerry")