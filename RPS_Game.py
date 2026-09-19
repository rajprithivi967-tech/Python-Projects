import random as rd
import time as td
print('='*9,'ROCK_PAPER_&_SCISSOR_GAME','='*9)
td.sleep(1)
countdown=3
def fun():
    try:
        print("\n1.ROUND OF 5\n2.ROUND OF 10\n3.CUSTOM ROUNDS\n")
        H=C=D=0
        n=int(input("\nEnter The Choice in integer : "))
        if n==1:
            a=5
        if n==2:
            a=10
        if n==3:
            a=int(input("\nEnter The Number Of Rounds (Any Wish ) : "))
        if n>3:
            print("\nENTER THE VALID ROUNDS\n")
            print("\n INITALIZING \n")
            td.sleep(1)
            fun()

        for i in range(0,a):
            print("\n1.ROCK\n2.PAPER\n3.SCISSORS\n")
            c=int(input("\nROCK,PAPER (OR) SCISSSORS :"))
            l=[1,2,3]
            g=rd.choice(l)
            if g==c:
                print("\nDRAW\n")
                D+=1
            if g==1 and c==2:#r&p
                print("\nHUMAN GOT A POINT \n\nCOMPUTER CHOICE IS :ROCK\nHUMAN CHOICE IS : PAPER \n")
                H+=1
            if g==1 and c==3:
                print("\nCOMPUTER GOT A POINT \n\nCOMPUTER CHOICE IS :ROCK\nHUMAN CHOICE IS :SCISSORS\n")
                C+=1
            if g==2 and c==1:
                print("\nCOMPUTER GOT A POINT \n\nCOMPUTER CHOICE IS :PAPER\nHUMAN CHOICE IS :ROCK\n")
                C+=1
            if g==2 and c==3:
                print("\nHUMAN GOT A POINT \n\nCOMPUTER CHOICE IS :PAPER\nHUMAN CHOICE IS :SCISSORS\n")
                H+=1
            if g==3 and c==1:
                print("\nHUMAN GOT A POINT \n\nCOMPUTER CHOICE IS :SCISSOR\nHUMAN CHOICE IS :ROCK\n")
                H+=1
            if g==3 and c==2:
                print("\nCOMPUTER GOT A POINT \n\nCOMPUTER CHOICE IS :SCISSORS\nHUMAN CHOICE IS :PAPER\n")
                C+=1
            if c>3:
                print("\nWARNING : Enter The Valid Range !!")
        print('\n','='*9,"RESULTS FOR THE ROUND",'='*9)
        
        print("\n Results in :3")
        td.sleep(1)
        print("\n Results in :2")
        td.sleep(1)
        print("\n Results in :1")
        td.sleep(1)

        
        print("\nHUMAN POINT : ",H)
        print("\nCOMPUTERS POINT : ",C)
        print("\nDRAWS : ",D)
        
        if H>C:
            print("\nHUMAN WON THE MATCH\n")

        if C>H:
            print("\nCOMPUTER WON THE MATCH\n")

        if C==H:
            print("\nMatch Draw\n")
        print("\nTHANK YOU FOR TRYING THIS OUT\n")
    except ValueError:
        print("\nWARNING : Enter The Valid Type !!\n")
        fun()

def choice():    
    print("\n1.Start\n\n2.Exit\n")
    try:
        ch=int(input("\nEnter The Choice To Begin The Game : "))
        while True:
            if ch==1:
                print("\nLOADING.....\n")
                td.sleep(2)
                fun()
                break
            if ch==2:
                print("\n EXITTING \n")
                td.sleep(2)
                print("\nThanks For Playing The Game\n")
                break
            if ch>2:
                print("\nWARNING : Enter The Valid Choice !!")
                choice()
    except ValueError:
        print("\nPlease Enter A Valid Type !\n")
        choice()
choice()    

    
