magic_number = 15;
numbers_taken = [1,7,12,19,22]
for x in range(0,20,5):
    if x is magic_number:
        print(x,' is a magic number')
        break
    else:
        print(x)
for v in range(25):
    if v in numbers_taken:
        continue
    print(v)