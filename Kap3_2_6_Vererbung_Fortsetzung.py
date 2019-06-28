class A:
    def m(self):
        print("m von A")

class B(A):
    def m(self):
        print("m von B")
        A.m(self)

class C(A):
    def m(self):
        print("m von C")
        A.m(self)

class D(B, C):
    def m(self):
        print("m von D")
        B.m(self)
        C.m(self)

d = D()
d.m()
