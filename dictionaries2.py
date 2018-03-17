stocks = {
    'GOOG':256.8,
    'APPL':128.9,
    'FB':167.1,
    'MST':212.5,
    'AMZ':230.0
}

print(min(stocks))
print(min(stocks.items()))
print(max(zip(stocks.values(),stocks.keys())))
print('\n')
print(sorted(stocks))
print(sorted(stocks.items()))
print(sorted(zip(stocks.values(),stocks.keys())))
