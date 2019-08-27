print( " WELCOME TO SAURAV's WORLD ")
print "\n"
name=raw_input("What is your name ?" )

print " INTRODUCTION "
print
print " In this world you can play the diffrent kinds of game."
print "  You can also do the calculation work "
print "  Here you will be provided with certain options "
print " which will help you to decide in wich field you want to go."
print
print " So let enter in Saurav's World...."
print
print " Press 1 to open the door and enter "
print
a=int(raw_input(" Enter '1' To open The door:"))
if a==1:
    print
    print " Welcome ",name ," TO Saurav's world"
    print
    def world(x):
        print " Press '1' for Paying game "
        print
        print " Press '2' for calculation "
        print
        print " Press '3' for Exit from SAURAV's WORLD "
        print
    n=1
    print world(2)
    while n>0:
            opt=int(raw_input(" Enter your choice :"))
            print
            if opt==1:
                print " Press '1' for Playing Hangman "
                print
                print " Press '2' for Playing Guessing Game "
                print
                print " Press '3' for Playing KBC "
                print
                b=int(raw_input(" Enter your choice:"))
                print
                if b==1:
                    print "                                                         Welcome to Hangman "
                    print
                    def sau(x):

                        print " For instruction press '1' "
                        print " For Playing Hangman press '2' "
                        print " Foe any help press '3' "

                    print sau(2)
                    print
                    print " hello",name
                    m=1
                    while m>0:

                        choice=int(raw_input("enter your choice:"))

                        if choice==1:
                            print " Instructions "
                            print " Computer will randomly select a word and you have to guess that word "
                            print " Thier will be two parts in the game you have to select any one"
                            print " Frist type will select a word releted to Litrature "
                            print " Secound will select word releted to computer "
                            print
                            print sau(2)

                        if choice==2:
                            import random
                            print " press '1' for Computer related words "
                            print " press '2' for Litrature related words "
                            print
                            opt=int(raw_input("enter your choice:"))
                            word=" "
                            if opt==1:

                                num=random.randint(1,4)
                                if num==1:
                                    word="moniter"
                                    print "hint"
                                    print " a hardware which display the output"
                                if num==2:
                                    word="python"
                                    print"hint"
                                    print" a programing language "
                                if num==3:
                                    word="motherboard"
                                    print"hint"
                                    print"main part of CPU "
                                if num==4:
                                    word="linux"
                                    print"hint"
                                    print"A operating System"

                            if opt==2:
                                num=random.randint(5,8)
                                if num==5:
                                    word="petard"
                                    print"hint"
                                    print" A small engine of war for breaking a barriers"
                                if num==6:
                                    word="petal"
                                    print" hint"
                                    print" A single leaflet of a corolla of a flower"
                                if num==7:
                                    word="vintage"
                                    print "hint"
                                    print" the time of gathering the crop of grapes"
                                if num==8:
                                    word="vigorous"
                                    print"hint"
                                    print" Full of physical strenght"

                            turn=7
                            s=" "

                            while turn>0:
                                failed=0

                                for chr in word:
                                    if chr in s:
                                        print chr
                                    else:
                                        print "_",
                                        failed=failed+1
                                if failed==0:
                                    print
                                    print name,"You won the game....."
                                    print " For exit press '9' or press any other number key to go on main screen "
                                    print " OR press '5' for exit from SAURAV's WORLD"
                                    num1=int(raw_input(" Enter your choice "))
                                    if num1==9:
                                        m=m-1
                                        print " Thanks for visiting...."
                                        print"\n"
                                        print world(2)
                                        break
                                    if num1==5:
                                        print " Thanks For Visiting In SAURAV's WORLD "
                                        n=n-1
                                        m=m-1
                                        break
                                    else:
                                        print sau(2)
                                        break
                                print
                                guess=raw_input("Enter a charecter:")
                                s=s+guess

                                if guess not in word:
                                    print "Wrong"
                                    turn=turn-1
                                    print
                                    print " you have left with",turn," more turn"
                                    if turn==0:
                                        print name," You loose the game....."
                                        print " Try Again "
                                        print " For exit press '9' or any other number key to go again on play screen "
                                        print "  OR press 5 for exit from SAURAV's WORLD "
                                        num1=int(raw_input(" Enter your choice "))
                                        if num1==9:
                                            m=m-1
                                            print " Thanks for visiting...."
                                            print"\n"
                                            print world(2)
                                        if num1==5:
                                            print " Thanks For visiting SAURAV's WORLD "
                                        else:
                                            print sau(2)


                        if choice ==3:
                            print " The hint will be displayed on the screen while playing"
                            print "  acoording to that hint you have to guess that word"
                            print " And one by one you have to guess a charecter "
                            print
                            print sau(2)

                if b==2:
                    print " Welcome to guessing game..."
                    print"\n"
                    print " Hints"
                    print"\n"
                    print " You have to guess a number if your guess matched with computers number than you will won the game othe wise you will loose the game\
                        you will be provided with 5 chance to guess that number.."
                    print"\n"
                    print " Hello ",name

                    import random

                    num=random.randint(100,200)



                    turn=1
                    while turn<6:
                        print
                        guess=int(raw_input("enter your guess between 100 to 200:"))
                        print
                        if guess==num:
                            print
                            print " You Won the Game....",name
                            print"\n"
                            print world(2)
                            break
                        if guess>num:
                            print
                            print " the number is too high "
                        else:
                            print
                            print " the number is too low "
                            turn=turn+1

                        if turn==6:
                            print"\n"
                            print " You loose the game....",name
                            print " The number was :",num
                            print"\n"
                            print world(2)



                if b==3:
                    print "***** WELLCOME TO KBC *****"
                    print "\n"

                    print "Hello ",name
                    print

                    print "Hints:"
                    print
                    print"You Will be asked with 7 question containg 4 options.\
                         you have to only tell the correct option number.\
                         correct answer will give you Rs 25,000 &  worng answer will reduce Rs 10,000."

                    print"\n"

                    print " so lets start the game ...."
                    print
                    print " press '7' to start the game "
                    print
                    start=int(raw_input("Enter your choice:"))
                    if start==7:

                        point=0
                        import time
                        print " So the frist question is on your screen "
                        time.sleep(1)
                        print

                        q1=''' (Q-1) Grand Central Terminal, Park Avenue, New York is the world's:

                        (a) largest railway station
                        (b) highest railway station
                        (c) longest railway station
                        (d) None of the above '''

                        print q1
                        print

                        ans=raw_input(" Enter your option :")

                        if ans=="a":
                            print
                            print " Your answer is correct"
                            print
                            point+=25000

                            print " Your total Money is:",point,"Rs"
                        else:
                            print
                            print " Your answer is wrong"
                            print
                            point-=10000

                            print " your total Money is :",point," Rs"
                        print
                        print " So the Second question is on your screen "
                        time.sleep(1)
                        print

                        q2=''' (Q-2) Entomology is the science that studies :

                        (a) Behavior of human beings
                        (b) Insects
                        (c) The origin and history of technical and scientific terms
                        (d) The formation of rocks '''

                        print q2
                        print

                        ans=raw_input(" Enter your option :")

                        if ans=="b":
                            print
                            print " Your answer is correct"
                            print
                            point+=25000

                            print " Your total Money is:",point,"Rs"
                        else:
                            print
                            print " Your answer is wrong"
                            print
                            point-=10000

                            print " your total Money is :",point," Rs"
                        print
                        print " So the Third question is on your screen "
                        time.sleep(1)
                        print

                        q3=''' (Q-3) FFC stands for :

                        (a) Foreign Finance Corporation
                        (b) Film Finance Corporation
                        (c) Federation of Football Council
                        (d) None of the above '''

                        print q3
                        print

                        ans=raw_input(" Enter your option :")

                        if ans=="b":
                            print
                            print " Your answer is correct"
                            print
                            point+=25000

                            print " Your total Money is:",point,"Rs"
                        else:
                            print
                            print " Your answer is wrong"
                            print
                            point-=10000

                            print " your total Money is :",point," Rs"
                        print
                        print " So the Fourth question is on your screen "
                        time.sleep(1)
                        print

                        q4=''' (Q-4) Galileo was an Italian astronomer who :

                        (a) developed the telescope
                        (b) discovered four satellites of Jupiter
                        (c) discovered that the movement of pendulum produces a regular time measurement
                        (d) All of the above '''

                        print q4
                        print

                        ans=raw_input(" Enter your option :")

                        if ans=="d":
                            print
                            print " Your answer is correct"
                            print
                            point+=25000

                            print " Your total Money is:",point,"Rs"
                        else:
                            print
                            print " Your answer is wrong"
                            print
                            point-=10000

                            print " your total Money is :",point," Rs"
                            print
                        print " So the Fiveth question is on your screen "
                        time.sleep(1)
                        print

                        q5=''' (Q-5) First human heart transplant operation conducted by Dr. Christian Bernard on Louis Washkansky, was conducted in :

                        (a) 1967
                        (b) 1968
                        (c) 1958
                        (d) 1922 '''

                        print q5
                        print

                        ans=raw_input(" Enter your option :")

                        if ans=="a":
                            print
                            print " Your answer is correct"
                            print
                            point+=25000

                            print " Your total Money is:",point,"Rs"
                        else:
                            print
                            print " Your answer is wrong"
                            print
                            point-=10000

                            print " your total Money is :",point," Rs"
                            print
                            print " So the Sixth question is on your screen "
                            time.sleep(1)
                            print

                        q6=''' (Q-6) Epsom (England) is the place associated with :

                        (a) Horse racing
                        (b) Polo
                        (c) Shooting
                        (d) Snooker '''

                        print q6
                        print

                        ans=raw_input(" Enter your option :")

                        if ans=="a":
                            print
                            print " Your answer is correct"
                            print
                            point+=25000

                            print " Your total Money is:",point,"Rs"
                        else:
                            print
                            print " Your answer is wrong"
                            print
                            point-=10000

                            print " your total Money is :",point," Rs"
                        print
                        print " So the Seventh question is on your screen "
                        time.sleep(1)
                        print

                        q7=''' (Q-7) Fastest shorthand writer was :

                        (a) Dr. G. D. Bist
                        (b) J.R.D. Tata
                        (c) J.M. Tagore
                        (d) Khudada Khan '''

                        print q7
                        print

                        ans=raw_input(" Enter your option :")

                        if ans=="a":
                            print
                            print " Your answer is correct"
                            print
                            point+=25000

                            print " Your total Money is:",point,"Rs"
                        else:
                            print
                            print " Your answer is wrong"
                            print
                            point-=10000

                            print " your total Money is :",point," Rs"
                        print


                        print " Congratulation ",name," You Finally Won ",point,"Rs"
                        print"\n"
                        print world(2)




            if opt==2:
                m=1
                while m>0:
                    print
                    print " press '1' For calculating the squar root of any number "
                    print
                    print " press'2' For printing table of any number "
                    print
                    print " press '3' For findind the square of any number "
                    print
                    print " Press '4' for exit "
                    print
                    b=int(raw_input("Enter your choice:"))
                    if b==1:
                        print
                        print " You have to enter the the number whoes square root you want to find "
                        print
                        num=float(raw_input("Enter the number:"))
                        print
                        import math
                        a=math.sqrt(num)
                        print
                        print " The square root is:",a
                        print
                        print " press 9 for Exit or press any other number key to go again on calculation screen"
                        again=int(raw_input("Enter your choice:"))
                        print
                        if again==9:
                            print " Thanks for visiting ...."
                            print
                            print world(2)
                            m=m-1
                            break

                    if b==2:
                        print
                        print" You have to enter the number whoes table you want to print "
                        num=int(raw_input(" Enter the number:"))
                        print
                        print " The table of the number is :-"
                        print"\n"
                        for a in range (1,11):
                            b=num*a
                            print
                            print num,"X",a,"=",b
                        print
                        print " press 9 for Exit or press any other number key to go again on calculation screen"
                        again=int(raw_input("Enter your choice:"))
                        print
                        if again==9:
                            print " Thanks for visiting ...."
                            print
                            print world(2)
                            m=m-1
                            break

                    if b==3:
                        print
                        print " You have to enter the number whoes square you want to find"
                        num=float(raw_input("Enter the number:"))
                        print
                        a=num**2
                        print" The square of the number is:",a
                        print
                        print " press 9 for Exit or press any other number key to go again on calculation screen"
                        again=int(raw_input("Enter your choice:"))
                        print
                        if again==9:
                            print " Thanks for visiting ...."
                            print
                            print world(2)
                            m=m-1
                            break
                    if b==4:
                        print
                        print " Thanks for visiting "
                        print
                        print world(2)
                        m=m-1
                        break



            if opt==3:
                print " Thanks for visiting in SAURAV's WORLD "
                n=n-1
                break

