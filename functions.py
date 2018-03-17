#no-argument definition
def ffff():
    print('Fuctions a re fffff')
    return 'cccccc'

print(ffff(),'\n')

#default-argument
def others_to_cse(curr_branch = 'mech'):
    print('leave ',curr_branch)
    print('learn programming')
    print('learn machine learning')
    print('do some projects ')
    print('get a job\n\n')

others_to_cse('civil')

#default-argument-->passing not all arguments
def  a_sentence(name = 'IT', action = 'is a',item = 'thop'):
    print(name,action,item)
a_sentence()
a_sentence(item = 'thurum')
a_sentence(name='tya',item='tiger')
