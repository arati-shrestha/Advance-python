
# import copy
# org = [[5,6],7,8] 
# cpy = copy.deepcopy(org)
# cpy[0][0] = 1
# print(cpy)
# print(org)


import copy
class Person:
    def __init__(self, name, age):
        self.name= name 
        self.age = age
        
class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee
    
    

p1 = Person('Alex', 27)
p2 = Person('joe', 22)

company = Company(p1,p2)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 56
print(company_clone.boss.age)
print(company.boss.age)


    