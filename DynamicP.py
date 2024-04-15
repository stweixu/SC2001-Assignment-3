def main():
    w1 = [4, 6, 8]
    p1 = [7, 6, 9]
    C1 = 14
    n1 = len(w1)

    total_profit_4a = profit_array(w1, p1, C1)
    recur_4a = recursive_func(w1, p1, C1, n1)

    print("--------Part 4a--------")
    print(f"P(14) using Recursion = {recur_4a}")
    print(f"P(14) using DP = {total_profit_4a}\n")

    w2 = [5, 6, 8]
    p2 = [7, 6, 9]
    C2 = 14
    n2 = len(w1)

    total_profit_2 = profit_array(w2, p2, C2)
    recur_4b = recursive_func(w2, p2, C2, n2)
    print("--------Part 4b--------")
    print(f"P(14) using Recursion = {recur_4b}")
    print(f"P(14) using DP = {total_profit_2}\n")


def profit_array(w, p, C):
    total_p = [0] * (C+1)

    for obj in range(len(w)):
        weight = w[obj]
        profit = p[obj]
        for capacity in range(C+1):
            if weight <= capacity:
                total_p[capacity] = max(total_p[capacity], total_p[capacity-weight] + profit)

    return total_p[C]


def recursive_func(w, p, C, n):
    if C == 0 or n == 0:
        return 0
    if w[n-1] > C:
        return recursive_func(w, p, C, n-1)
    else:
        return max(recursive_func(w, p, C-w[n-1], n) + p[n-1], recursive_func(w, p, C, n-1))


if __name__ == "__main__":
    main()
