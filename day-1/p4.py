'''wirte a program in which to bulid login system using functions.The function main should be login regrsiter
1.you should ask user to enter the detail for regestration and out of all these details only username and password should be stored
2.now this function to enter username and password.If these match with the registred details login succes otherwise repeat the login process same the invalid craditionals until they right'''
def loginandreg():
    d=()
    print("welcome to registration")
    u_name=input("enter username")
    u_password=input("enter password")
    name=input("enter name")
    phone=input("enter phone no")
    
    d[u_name]=u_password
    
    while True:
        print("welcome to login")
        
        l_name=input("enter login username")
        l_password=input("enter login uesr password")
