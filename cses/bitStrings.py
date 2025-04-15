MOD = 10**9 + 7

def power(base, exp):
    result = 1
    while exp > 0:
        note = ""
        if exp % 2 == 1:
            result = (result * base) % MOD
            note = "exp lẻ → nhân vào result"
        else:
            note = "exp chẵn → không nhân"

        base = (base * base) % MOD
        exp //= 2

    return result

# Nhập giá trị n
n = int(input())
print(power(2, n))
