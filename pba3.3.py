
password = input("Enter Password: ")

n = len(password)

# DP states
dp = [[False] * 4 for _ in range(n + 1)]

dp[0][0] = True

for i in range(n):
    ch = password[i]

    for j in range(4):
        if dp[i][j]:
            dp[i + 1][j] = True

    if ch.isupper():
        dp[i + 1][1] = True

    if ch.isdigit():
        dp[i + 1][2] = True

    if ch in "!@#$%^&*":
        dp[i + 1][3] = True

# Validate all conditions
if n >= 8 and dp[n][1] and dp[n][2] and dp[n][3]:
    print("Valid Password")
else:
    print("Invalid Password")
