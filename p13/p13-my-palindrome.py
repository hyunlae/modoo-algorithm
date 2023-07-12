# 주어진 문장이 회문인지, 아닌지 찾기(큐와 스택의 특징을 이용)
# 입력 문자멸 s
# 출력: 회문이면 True, False

def palindrome(s):
    st = []

    for x in s:
        if x.isalpha():
            st.append(x.lower())

    mid = len(st) // 2
    for i in range(0, mid):
        if st[i] != st[len(st) - 1 - i]:
            return False

    return True


print(palindrome("Wow"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I am Adam."))
