import random as rd
def fun():
    while True:
        ch=input("roll the dice ? (y/n) ")
        if ch in'Yy':
            a=rd.randint(1,6)
            b=rd.randint(1,6)
            c=(a,b)
            print(c)
        if ch in 'Nn':
            print("Thanks For Playing")
            break
        if ch not in 'YyNn':
            print("Invalid Option")
fun()
        
        
