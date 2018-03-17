magic_number = int(input('Enter your magic number:'))
numbers_taken = [1,7,12,19,22]
for x in range(20):
    if x is magic_number:
        print(x ,' is your magic number')
        break
    else:
        print(x)
for v in range(25):
    if v in numbers_taken:
        continue
    print(v)