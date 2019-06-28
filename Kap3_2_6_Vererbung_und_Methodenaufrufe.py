class A:
    def m(self):
        print("m von A")

class B(A):
    def m(self):
        print("m von B")

class C(A):
    def m(self):
        print("m von C")

class D(B, C):
    def m(self):
        print("m von D")

d = D()
A.m(d)
C.m(d)
B.m(d)
D.m(d)
