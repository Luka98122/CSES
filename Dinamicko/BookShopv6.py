# import sys

# sys.stdin = open("test1.txt")


def maximum_number_pages(max_price, n, books):
    max_pages = [0] * (max_price + 1)
    counter = 1
    for price, count in books:
        for i in range(max_price, price - 1, -1):
            max_pages[i] = max(max_pages[i], max_pages[i - price] + count)
        counter += 1
    print(max_pages[max_price])
    exit()


n, max_price = map(int, input().split())
prices = list(map(int, input().split()))
number_pages = list(map(int, input().split()))
books = list(zip(prices, number_pages))


maximum_number_pages(max_price, n, books)
# time.sleep(0.9)
# exit()
