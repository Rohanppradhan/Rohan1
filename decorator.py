def ext_pro(func):
    def in_operations():
        print("this is inner function of decorations")
        func()
    return in_operations

@ext_pro
def print_fun():
    print("I am Function")
print_fun()    