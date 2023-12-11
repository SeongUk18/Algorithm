import sys
import heapq

n = int(sys.stdin.readline())

books = {}
sort_book = []

for _ in range(n):
    book = sys.stdin.readline()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

for book_name, count in books.items():
    heapq.heappush(sort_book, (-count, book_name))


print(heapq.heappop(sort_book)[1])