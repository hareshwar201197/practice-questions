
def my_decorator(func):
    def wrapper():
        print('before function call')
        func()
        print('after function call')
    return wrapper

@my_decorator
def hello_decorator():
    print('decorator function practice')

hello_decorator()