import random
import time
import os
clear = lambda: os.system('cls')

#s="+ - - - - +"
s=""
m1="  o   o  "
m2="  o      "
m3="    o    "
m4="      o  "
m5="         "

def side_1():
    print(m5)
    print(m3)
    print(m5)

def side_2():
    print(m5)
    print(m1)
    print(m5)

def side_3():
    print(m2)
    print(m3)
    print(m4)

def side_4():
    print(m1)
    print(m5)
    print(m1)

def side_5():
    print(m1)
    print(m3)
    print(m1)

def side_6():
    for i in range(1,4):
        print(m1)

def choice(a):
        if a==1:
            print(s)
            side_1()
            print(s)
        elif a==2:
            print(s)
            side_2()
            print(s)
        elif a==3:
            print(s)
            side_3()
            print(s)
        elif a==4:
            print(s)
            side_4()
            print(s)
        elif a==5:
            print(s)
            side_5()
            print(s)
        else:
            print(s)
            side_6()
            print(s)

def intro():    
    print("************WELCOME TO THE GAME*************")
    print("MENU")
    print("PRESS A FOR SINGLE PLAYER ")
    print("PRESS B FOR MULTIPLAYER ")
    print("PRESS E TO EXIT")
    return input().upper()

def dikha_jalwa(player):
    for i in range(1,15):
        clear()
        print("PLAYER %d" %player)
        time.sleep(1/14)
        choice(random.randrange(1,7,1))
        time.sleep(1/14*2)
    clear()
        
        

def decide(a,b):
    if a>b :
        return True
    else:
        return False

def single_player():
    print("YOU ARE PLAYING AGAINST COMPUTER")
    print("YOU PLAY FIRST!!")
    time.sleep(1)
    clear()
    score_1=0
    score_2=0
    for i in range(1,6):                
            print("YOUR TURN\nPRESS ENTER TO CONTINUE or E TO ENDGAME ")
            if input().upper()!='E':
                    dikha_jalwa(1)
                    a = random.randrange(1,7,1)
                    print("PLAYER 1")
                    choice(a)
                    score_1+=a
                    print("THATS A %d " %a)
                    print("YOUR TOTAL SCORE IS %d " %score_1)
                    print("THE COMPUTER'S SCORE IS %d " %score_2)
                    time.sleep(0.5)
                    input("PRESS ENTER TO CONTINUE ")
                    clear()
                    print("COMPUTER'S TURN PLEASE WAIT...!")
                    time.sleep(1.5)
                    dikha_jalwa(2)
                    a = random.randrange(1,7,1)
                    print("PLAYER 2")
                    choice(a)
                    score_2 += a
                    print("THATS A %d " %a)
                    print("COMPUTER'S TOTAL SCORE IS %d " %score_2)
                    print("YOUR SCORE IS %d" %score_1)
                    time.sleep(2)
                    input('PRESS ENTER TO CONTINUE')
                    clear()
            else:
                break
    if decide(score_1,score_2):
        print("YOU WIN!!! :)")
    else:
        print("OH NO!!! YOU LOSE.. :( ")
    print("DO YOU WANT TO PLAY AGAIN!! ")
    time.sleep(2)
    print("PRESS ANY KEY TO CONTINUE OR 'E' TO EXIT ")
    if input().upper()!='E':
        clear()
        main()
    else:
        call_end()


def multi_player():
    score_1 = 0
    score_2 = 0
    for i in range(1,6):
        print("PLAYER 1 TURN\nPRESS ANY KEY TO ROLL THE DICE AND 'E' TO EXIT")
        if input().upper() != 'E':
            dikha_jalwa(1)
            a = random.randrange(1,7,1)
            print("PLAYER 1")
            choice(a)
            score_1+=a
            print("THATS A %d "%a)
            print("PLAYER 1 SCORE %d" %score_1)
            print("PLAYER 2 SCORE %d" %score_2)
            time.sleep(.5)
            input('ENTER ANY KEY TO CONTINUE')
            clear()
            print("PLAYER 2 TURN..PLEASE WAIT!!")
            time.sleep(1.5)
            dikha_jalwa(2)
            a = random.randrange(1,7,1)
            print("PLAYER 2")
            choice(a)
            score_2 += a
            print("THATS A %d" %a)
            print("PLAYER 1 SCORE %d" %score_1)
            print("PLAYER 2 SCORE %d" %score_2)
            time.sleep(.5)
            input("PRESS ENTER TO CONTINUE ")
            clear()
        else:
            break
    if decide(score_1,score_2):
        print("PLAYER 1 WINS")
    else:
        print("PLAYER 2 WINS")
    print("DO YOU WANT TO PLAY AGAIN!! ")
    time.sleep(2)
    print("PRESS ANY KEY TO CONTINUE OR 'E' TO EXIT ")
    if input().upper()!='E':
        clear()
        main()
    else:
        call_end()
            
def loading():
    clear()
    print("Loading")
    time.sleep(.3)
    clear()
    print("Loading.")
    time.sleep(.3)
    clear()
    print("Loading..")
    time.sleep(.3)
    clear()
    print("Loading...")
    time.sleep(.3)
    clear()
    
    
def loading_times(a):
    for i in range(0,a):
        loading()

def call_end():
    print("THANK YOU")
    time.sleep(2)


def main():
    loading_times(3)
    ch = intro()
    clear()
    loading_times(2)
    if ch == 'A':
        single_player()
    elif ch=='B':
        multi_player()
    else:
        call_end()
                        
      


main()       
