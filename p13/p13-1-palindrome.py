# 주어진 문장이 회문인지, 아닌지 찾기(큐와 스택의 특징을 이용)
# 입력 문자멸 s
# 출력: 회문이면 True, False

def palindrome(s):
    qu = []
    st = []

    for x in s:
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())

    while qu:
        if qu.pop(0) != st.pop():
            return False

    return True


print(palindrome("Wow"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I am Adam."))
