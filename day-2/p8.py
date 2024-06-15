class cse1:
    def __init__(self,a,b):
        self.a1=a
        self.b1=b
        print("i am constructor")
    def strenth(self):
        print("The strenth is 101")
        self.s=101
    def kn(self,c,d):
        print("the knowledge is good")
        self.know="good"
        pro=c+d
        print(pro)
    def details(self):
        print("the current strength and the knowledge")
        c_s=self.s=10
        print(c_s,self.know)
        print(self.a1+self.b1)

o=cse1(20,30)
print("below functions calls")
o.strenth()
o.kn(1,3)
o.details()

