H, M = map(int, input().split())

if H > 0 and M < 45:
    M = 60 + M - 45
    H -= 1
elif H == 0 and M < 45:
    M = 60 + M - 45
    H = 23
elif H == 0 and M >= 45:
    M -= 45
else:
    M -= 45

print(H, M)