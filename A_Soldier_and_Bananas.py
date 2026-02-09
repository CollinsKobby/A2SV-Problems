k, n, w = map(int, input().split(' '))

payment_price = 0

for i in range(1, w + 1):
    payment_price += i*k

amount = payment_price - n

if n >= payment_price:
    print('0')
else:
    print(amount)