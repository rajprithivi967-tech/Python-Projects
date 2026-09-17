print("="*9,"CALCULATOR PROGRAM",'='*9)
def calc():

    while True:
        cc=0
        a=int(input("enter the no A:"))
        b=int(input("enter the no B:"))

        print("1.add\n2.sub\n3.mul\n4.div")
        ch=int(input("enter the choice in intger : "))

        if ch==1:
            print("the add is :",a+b)

        if ch==2:
            print("the Sub is :",a-b)

        if ch==3:
            print("the Mul is :",a*b)

        if ch==4:
            print("the Div is :",a//b)
        cc+=1
        print("="*9,"PROGRAM_",cc,"_FINISHED",'='*9)
        A=input("another operation ? y/n :")
        if A in 'nN':
            print("EXITTING")
            break
        
calc()
