
''''
class Parent:
        last_name = ' Stark'
class child(Parent):
    def __init__(self,name):
        self.first_name = name
        print(self.first_name+self.last_name)

rob = child('Robb')
jon = child('Jon')

'''
class Father:
    f_name = ' Stark'
class Mother:
     m_name = ' Tully'
class child(Father,Mother):
    def __init__(self,name):
        self.name = name
        print(self.name+self.f_name+self.m_name)

rob = child('Robb')
jon = child('Jon')
