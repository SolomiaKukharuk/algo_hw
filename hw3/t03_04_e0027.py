def max_cyclic_shift(n):
    bin_str = bin(n)[2:]
    max_value = n
    for _ in range(len(bin_str) - 1):
        bin_str = bin_str[1:] + bin_str[0]
        max_value = max(max_value, int(bin_str, 2))
    return max_value

n = int(input().strip())
print(max_cyclic_shift(n))