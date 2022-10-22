from cmath import pi, sin
import numpy
class C:
    def __init__(self,first,sec):
        self.real1=first.real
        self.imag1=first.imag
        self.real2=sec.real
        self.imag2=sec.imag
        self.first=first
        self.sec=sec


    def add(self):
        a=self.first+self.sec
        print("the addition of the number is:",a)



    def distance(self):
        a=((self.real1-self.real2)**2)+((self.imag1-self.imag2)**2)
        a=a**0.5
        print("the distance between the number is :",a)



    def angle(self):
        a=numpy.arctan((self.imag1/self.real1))
        print("the angle of first number in degree is:",a*(180/pi))
        b=numpy.arctan((self.imag2/self.real2))
        print("the angle of second number in degree is:",b*(180/pi))


    def mul(self):
        a=self.first*self.sec
        print("the multiplication is :",a)


    def sub(self):
        a=self.first-self.sec
        print("the subtraction of two numbers is :",a)


    
    
a=complex(input("enter first complex no:"))
b=complex(input("enter second complex no:"))
z=C(a,b)
print("1:for add,2:for distance,3:for angle,4:for multiplication,5:for subtraction")
k=int(input("enter the subject:"))
if k==1:
    z.add()
elif k==2:
    z.distance()
elif k==3:
    z.angle()
elif k==4:
    z.mul()
elif k==5:
    z.sub()
else:
    print("invalid output")


