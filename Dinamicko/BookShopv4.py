import time

time_start = time.perf_counter()
grid = []

l1 = input().split()

n_books = int(l1[0])
budget = int(l1[1])

for i in range(n_books):
    grid.append([])
    for j in range(budget + 1):
        grid[i].append(0)

l2 = input().split()
l3 = input().split()
## 0.0855


books = []
for i in range(n_books):
    books.append([])
    books[i].append(int(l2[i]))
    books[i].append(int(l3[i]))
## 0.0936


time_start = time.perf_counter()
for i in range(n_books):
    if i == 4:
        a = 2
    for w in range(budget + 1):
        if w < books[i][0]:
            grid[i][w] = grid[i - 1][w]
        else:
            grid[i][w] = max(books[i][1] + grid[i - 1][w - books[i][0]], grid[i - 1][w])
    a = 2

## 0.6000
time_elapsed = time.perf_counter() - time_start
print(f"Elapsed: {time_elapsed}")

print(grid[-1][-1])
a = 2
