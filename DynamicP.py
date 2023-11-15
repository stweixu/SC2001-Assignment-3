def main():
    w1 = [4, 6, 8]
    p1 = [7, 6, 9]
    C1 = 14
    n1 = len(w1)
    total_profit_1 = profit_array(w1, p1, C1, n1)
    print_profit_array(C1, n1, total_profit_1)

    w2 = [5, 6, 8]
    p2 = [7, 6, 9]
    C2 = 14
    n2 = len(w1)
    total_profit_2 = profit_array(w2, p2, C2, n2)
    print_profit_array(C2, n2, total_profit_2)

    print(recursive_func(w2, p2, 14, 3))


def profit_array(w, p, C, n):
    total_p = [[0] * (n+1) for _ in range(C+1)]

    for i in range(1, C+1):
        total_p[i][0] = 0

    for i in range(1, n+1):
        total_p[1][i] = 0

    for capacity in range(1, C+1):
        for num_obj in range(1, n+1):

            total_p[capacity][num_obj] = total_p[capacity][num_obj-1]

            for index in range(num_obj):
                weight = w[index]
                profit = p[index]
                if weight <= capacity:
                    new_profit = total_p[capacity-weight][num_obj] + profit
                    if total_p[capacity][num_obj] <= new_profit:
                        total_p[capacity][num_obj] = new_profit
    return total_p


def print_profit_array(C, n, total_profit):
    for i in range(C+1):
        s = "Row " + str(i)
        print("{:<8s}".format(s), end="")
        for m in range(n+1):
            print(f"{total_profit[i][m] : ^3}", end=" ")
        print()
    print()


def recursive_func(w, p, C, n):
    if C == 0 or n == 0:
        return 0
    if w[n-1] > C:
        return recursive_func(w, p, C, n-1)
    else:
        return max(recursive_func(w, p, C-w[n-1], n) + p[n-1], recursive_func(w, p, C, n-1))


if __name__ == "__main__":
    main()
