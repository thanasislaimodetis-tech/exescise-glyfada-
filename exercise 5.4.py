def arithmetic_sum(a, d, n):
    total_sum = 0
    for i in range(n):
        term = a +(i * d)
        total_sum = total_sum + term
    return total_sum
if __name__ == "__main__":
    print(arithmetic_sum(1, 1, 100))
    print(arithmetic_sum(3, 2, 15))
    print(arithmetic_sum(10, 4, 5))
    print(arithmetic_sum(-5, -2, 20))