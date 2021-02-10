import random

print("what is your name: ")
name=input()
print("hello "+name+"\n **** welcome to hangman ****")
print("**** guss the word game ****")
s=('star','hello','cool','bigbang','bigboss','youtube','google','facebook')
r=random.choice(s)
g=''
ch=int(input("how many life you need"))
while ch>0:
    f=0
    for c in r:
        if c in g:
            print(c)
        else:
            print('-')
            f+=1
    if f==0:
        print("you win")
        break
    gs=input("guss the letter")
    if gs in r:
        g+=gs
    else:
        ch-=1
        print(f"oops you loss one life \n now you have {ch}")
    if ch==0:
        print("you lose")
        print("the letter is "+r)
        break




