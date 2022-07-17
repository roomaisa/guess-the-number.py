import  random



number=random.randint(1,100)
atempt=1
guess=int(input("enter number"))

while(True):

 if(guess>number):
    guess=int(input("enter number.this is too big:"))
    atempt += 1

 elif (guess<number):
    guess=int(input("enter number . this is too less:"))
    atempt += 1
 else :
    print(f" you won!.you guessed it right in {atempt} attempts")

    break




