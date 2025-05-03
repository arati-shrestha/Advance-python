#function that returns an object that can be iterated over: generate items inside object only when you ask for it. Memory efficient.

# def mygenerator():
#     yield 3
#     yield 2
#     yield 1

# g= mygenerator()


# print(sorted(g))

# for i in g:
#     print(i)
# def countdown(num):
#     print("starting")
#     while num > 0:
#         yield num
#         num -= 1
# cd = countdown(4) 
# value =  next(cd)

# print(value)
# print(next(cd))
# print(next(cd))
# print(next(cd))
# print(next(cd))
import sys 
# def firstn(n):
#     nums = []
#     num = 0
#     while num < n:
#         nums.append(num)
#         num +=1
#     return nums


# def first(n):
#     num = 0
#     while num<n:
#         yield num 
#         num += 1

# print(sys.getsizeof(firstn(1000)))
# print(sys.getsizeof(first(1000)))

# def fibonacci(limit):
#     a, b = 1,2
#     while a<limit:
#         yield a
#         a, b = b, a+b
    
# fib = fibonacci(40)
# for i in fib:
#     print(i)

mygenerator = (i for i in range(300) if i % 2 ==0)
print(sys.getsizeof(mygenerator))

lists = [i for i in range(300) if  i%2 ==0]
print(sys.getsizeof(lists))


