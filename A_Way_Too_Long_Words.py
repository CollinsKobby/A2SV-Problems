n = int(input())

for i in range(n):
    words = input()
    if len(words) > 10:
        print(f"{words[0]}{len(words[1:-1])}{words[-1]}")
    else:
        print(words)