#args = arguements, kwargs = keyword arguments

# def foo(a,b, *args, **kwargs):    #args take tuple as value and kwargs take dictionary formatted value
#     print(a,b)
#     for arg in args:
#         print(arg)
#     for key in kwargs:
#         print(key, kwargs[key])
        
# foo(1,2,3,4,5, name = '= arati')

# def fun(*args,last):
#     for arg in args:
#         print(arg)
#     print(last)
# fun(1,3,last = 2)

# def foo(a,b,c,d):
#     print(a, b, c,d)

# # my_list = (0,1,2)
# # foo(*my_list)

# my_dict = {'a':'my','b':'name','c':'is', 'd':'arati'}
# foo(**my_dict)


# my_tuple = (1,2,3)
# my_list = [4,5,6]


# new_list = [*my_tuple,*my_list]


# a_dict = {'a':'arata', "b":'boata'}
# b_dict = {'c':'aratb', "d":'boatb'}
# c_dict = {'e':'aratc', "f":'boatc'}
# new_dict = {**a_dict, **b_dict, **c_dict}
# print(new_dict)

# print(new_list)

def foo():
    global number 
    x = number
    number = 3
    
    print('number inside function:', x)



number = 0

print(number)
foo()

#Call by object or call by object reference: by reference 

def foo(x):
    x.append(4)
    
a = [1,2,3]

foo(a)
print(a)
