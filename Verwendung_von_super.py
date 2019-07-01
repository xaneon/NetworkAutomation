class A:
    def m(self):
        print("m von A")

class B(A):
    def m(self):
        print("m von B")
        super().m()

class C(A):
    def m(self):
        print("m von C")
        super().m()

class D(B, C):
    def m(self):
        print("m von D")
        super().m()

d = D()
d.m()
