class A:
    def __init__(self,name):
        self.name=name

    def q(self):
        print("name is ",self.name)

class B(A):
    def __init__(self, branch):
        self.branch=branch

    def w(self):
        print("branch is ",self.branch)

class C(B):
    def __init__(self,tech):
        self.tech=tech

    def e(self):
        print("techinical society is ",self.tech)

class D(B):
    def __init__(self, cultural):
        self.cultural=cultural

    def r(self):
        print("cultural society is ",self.cultural)

class E(D,C):
    def __init__(self, rollno):
        self.rollno=rollno

    def t(self):
        print("rollno is ",self.rollno)

a=E(2100271530015)
a.branch="cse (aiml)"
a.cultural="goonj"
a.name="Aniket"
a.tech="BRL"
a.q()
a.w()
a.e()
a.r()
a.t()