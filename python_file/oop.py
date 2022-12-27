# self có thể cả class hoặc instant của class (eg: emp_1) trong khi class thì chỉ cụ thể cả class chứ k chỉ từng instant riêng biệt :v
#regular method takes the arguments as an instant
#class method thì tương tự nhgma thay vì instant thì dùng class

#cái trước phụ thuộc vào cái sau thì tự động thay đổi theo
#nếu muốn là chiều ngược lại hoặc muốn thay đổi mà ko ảnh hưởng tới giá trị ban đầu (java??) thì ta dùng setter

class Employee:
    raise_amt = 1.04
    num_of_instant = 0
    def __init__(self, first, last, pay):
        self.first= first
        self.last = last
        self.pay = pay
        
        
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last) 

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last) 

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt) #getter & setter are better
        #there is a big difference between self instant and class instant
        #access a class instant through the class itself or through a instant of the class 
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None
    

emp_1 = Employee('John' ,'Smith', 200)
emp_1.first = 'Jill'

print(emp_1.email)
print(emp_1.first)
print(emp_1.last)

del emp_1.fullname

print(emp_1.email)
print(emp_1.first)
print(emp_1.last)








