
def star_end_decorator(func):
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper    

@star_end_decorator #does samething as : print_name = star_end_decorator(print_name)

def add5(x):
    return x+5
result = add5(10)
print(result)


# def print_name():
#     print("arati")


# print_name()
