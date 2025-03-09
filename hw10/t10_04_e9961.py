def generate_permutations(n, k):
    numbers = list(range(1, n + 1))
    used = [False] * (n + 1)
    current_permutation = []
    results = []

    def backtrack():
        if len(current_permutation) == k:
            results.append(" ".join(map(str, current_permutation)))
            return

        for i in range(n):
            if not used[i + 1]:
                used[i + 1] = True
                current_permutation.append(numbers[i])
                backtrack()
                current_permutation.pop()
                used[i + 1] = False
    backtrack()
    return results



n, k = map(int, input().split())

results = generate_permutations(n, k)
for perm in results:
    print(perm)