import random as rd
print('='*9,"NUMBER GUESSING GAME",'='*9)
def fun():
    a=rd.randint(1,100)
    while True:
        b=int(input("Guess The Number :"))
        if a>b:
            print("Too Low !")
        if a<b:
            print("Too High !")
        if a==b:
            print("Congrats You Have Found The Number & The Number Is :",a)
            break
        if b>100 or b==0:
            print("Guess The Number Btw The Give Range Bro")
    
print("1.Start/n2.Exit")
ch=int(input("Enter The Choice To Begin The Game"))
if ch==1:
    fun()
if ch==2:
    print("Thanks For Playing The Game")
