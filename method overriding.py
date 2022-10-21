class A:
    def method1(self):
        print("Parent Class Method")
class B(A):
    def method2(self):
        print("Child Class is")
b=B()
b.method1()
b.method2()

