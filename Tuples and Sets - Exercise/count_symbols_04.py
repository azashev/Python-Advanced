input_line = input()

symbols_count = {}

for symbol in input_line:
    if symbol not in symbols_count:
        symbols_count[symbol] = 0
    symbols_count[symbol] += 1

for symbol, count in sorted(symbols_count.items()):
    print(f"{symbol}: {count} time/s")
