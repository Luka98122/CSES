def main(max_price, prices, number_pages, n_books):
    res = [0] * (max_price + 1)
    for j in range(n_books):
        for i in range(max_price, prices[j] - 1, -1):
            res[i] = max(res[i], res[i - prices[j]] + number_pages[j])
    return res[-1]


l1 = input().split()
n = int(l1[0])
max_price = int(l1[1])

prices = list(map(int, input().split()))
number_pages = list(map(int, input().split()))

print(main(max_price, prices, number_pages, n))
