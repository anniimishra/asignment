from cmath import pi
def volume(a,b=None,c=None):
    if a==b==c:
        print("volume of the cube id",a**3)
    elif c==None and b!=None:
        print("volume of the cylinder is ",pi*a*a*b)
    elif c==None and b==None:
        print("volume of sphere is",pi*a*a*a*(4/3))
    else:
        print("volume of cuboid is",a*b*c)


volume(2)
volume(2,3,4)
volume(2,3)
volume(2,2,2)