prices = {"apple": 50, "banana": 30, "cherry": 70, "fig": 40}
expensive_product = max(prices, key=prices.get)
cheap_product = min(prices, key=prices.get)
by_price = dict(sorted(prices.items(), key=lambda kv: kv[1]))

print(f'{expensive_product}\n{cheap_product}\n{by_price}')


