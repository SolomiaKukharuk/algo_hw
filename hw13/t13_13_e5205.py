def safe_count_valid_sequences(template: str, mod=301907):
    n = len(template)
    max_bal = n
    dp = [[0] * (max_bal + 2) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(n):
        for bal in range(max_bal + 1):
            if dp[i][bal] == 0:
                continue

            ch = template[i]
            if ch == '(':
                if bal + 1 <= max_bal:
                    dp[i + 1][bal + 1] = (dp[i + 1][bal + 1] + dp[i][bal]) % mod
            elif ch == ')':
                if bal > 0:
                    dp[i + 1][bal - 1] = (dp[i + 1][bal - 1] + dp[i][bal]) % mod
            elif ch == '?':
                if bal + 1 <= max_bal:
                    dp[i + 1][bal + 1] = (dp[i + 1][bal + 1] + dp[i][bal]) % mod
                if bal > 0:
                    dp[i + 1][bal - 1] = (dp[i + 1][bal - 1] + dp[i][bal]) % mod

    return dp[n][0]


def main():
    import sys
    template = sys.stdin.read().strip()
    print(safe_count_valid_sequences(template))


if __name__ == "__main__":
    main()