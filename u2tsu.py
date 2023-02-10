class A:

    def __init__(self, mam1, mam2):
        self.mam1 = mam1
        self.mam2 = mam2

    def metod1(self):
        print("metod_1 class A")

    def metod2(self):
        print("metod_2 class A")

    def metod3(self):
        print("metod_3 class A")

class B(A):
    def __init__(self, mam1, mam2, mam3):
        super().__init__(mam1, mam2)
        self.mam3 = mam3

    def metod3(self):
        print("metod 3 class B")

class C(A):
    def __init__(self, mam1 = "default_nam1", mam2 = "default_nam2"):
        super().__init__(mam1, mam2)

    def metod4(self):
        print("metod_4 class C")

    def metod5(self):
        print("metod_5 class C")

a = A("mam1_value", "mam2_value")
b = B("mam1_value", "mam2_value", "mam3_value")
c = C()

a.metod1()
a.metod2()
a.metod3()

b.metod1()
b.metod2()
b.metod3()

c.metod1()
c.metod2()
c.metod3()
c.metod4()
c.metod5()