
class Faculty:#parent class
     def __init__(self,f_name,department,f_id):
         self.f_name=f_name
         self.department=department
         self.f_id=f_id
     def print_info(self):
         print('faculty information',self.f_name,self.department,self.f_id)
obj=Faculty("Sidd","Computer_Science",1001)
obj.print_info()
#===========================================================================
#class chile_classname(parent_classname)
class cse(Faculty): #child class
    pass
obj1=cse("Sidd","computer_science",1002)
obj1.print_info()
#===========================================================================
#Multiple inheritance
class SubMarks: #class-1
    math=int(input("Enter paper marks of maths:"))
    DE=int(input("Enter paper marks of Design Engineering:"))
    C=int(input("Enter the paper marks of C Language:"))
    English=int(input("Enter paper marks of English:"))
#=================== Parent class 1
class PractMarks: #class-2
    cpract=int(input("Enter practical marks of c language:"))
#=================== Parent class 2
class Result(SubMarks,PractMarks): #Child Class
    def total(self):
        if self.math>=40 and self.DE>=40 and self.C>=40 and self.English>=40:
            print("pass")
            
        else:
            print("Fail")
obj2=Result()
obj2.total()
#============================================================================
#================================OUTPUT======================================
'''
faculty information Sidd Computer_Science 1001
faculty information Sidd computer_science 1002
Enter paper marks of maths:90
Enter paper marks of Design Engineering:98
Enter the paper marks of C Language:99
Enter paper marks of English:99
Enter practical marks of c language:100
pass
'''

