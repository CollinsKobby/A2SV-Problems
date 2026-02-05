import sys

lines = sys.stdin.read().strip().split('\n')
n = int(lines[0])

phone_book = {}
for i in range(1, n + 1):
    name, phone = lines[i].split()
    phone_book[name] = phone

for query in lines[n + 1:]:
    if query in phone_book:
        print(f"{query}={phone_book[query]}")
    else:
        print("Not found")
