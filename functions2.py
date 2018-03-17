#variable arguments
'''
def sum(*args):
    total = 0
    for a in args:
        total = a + total
    return total

print(sum(3,4,5))
print(sum(1))
print(sum(34,89,12121212))
'''
#health - calculator --> unpacking arguments

def health_calc(age = 20,apples = 1,cigars = 5):
    lifetime = (100-age) + (apples*2) - (cigars*0.5)
    print(lifetime)

bucky_data = [19,2,5]

health_calc(27,0,0)
health_calc()
health_calc(*bucky_data)
