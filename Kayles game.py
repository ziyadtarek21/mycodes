desscion=1
while desscion==1:
 checker1=0
 checker2=0
 n=int(input("how many numbers of tokens in the row "))
 while n<=0:
    print("sorry wrong input enter a number more than 0")
    n = int(input(" how how many numbers of tokens in the row "))
 tokens=list()
 desscion1=0
 for i in range(1,n+1):
    tokens.append(i)


 while(True):

        print(tokens)
        player1=input(" player1 choose a token number ").split()
        while len(player1)<1 or len(player1)>2 :
            print("sorry wrong input you cant choose more than two tokens or less than one toke")
            player1 = input(" player1 choose a token number ").split()
        if len(player1)>1:
            for i in tokens:
                for m in player1:
                 if int(m)==int(i):
                    checker1+=1
            while checker1<2:
                print("you choosed a number which is not found in the list please choose again wisely")
                player1 = input(" player1 choose a token number ").split()
                for i in tokens:
                    for m in player1:
                        if int(m) == int(i):
                            checker1 += 1

            tokens.remove(int(player1[0]))
            tokens.remove(int(player1[1]))
        else:
            for i in tokens:
                if int(player1[0])==int(i):
                    checker1+=1
            while checker1<1:
                print("you choosed a number not found in the list please choose again wisely")
                player1=input(" player1 choose a token number ").split()
                for i in tokens:
                    if int(player1[0]) == int(i):
                        checker1 += 1

            tokens.remove(int(player1[0]))

        if len(tokens)==0:
            print("player 1 wins")
            break

        else:
         player2=input(" player2 choose a token number ").split()
         while len(player2)<1 or len(player2)>2:
             print("sorry wrong input you cant choose more than two numbers or less than one number ")
             player2= input(" player2 choose a token number ").split()
         if len(player2)>1:
            for i in tokens:
                for m in player2:
                 if int(m)==int(i):
                    checker2+=1
            while checker2<2:
                print("you choosed a number which is not found in the list please choose again wisely")
                player2= input(" player2 choose a token number ").split()
                for i in tokens:
                    for m in player2:
                        if int(m) == int(i):
                            checker2 += 1
            tokens.remove(int(player2[0]))
            tokens.remove(int(player2[1]))
         else:
             for i in tokens:
                 if int(player1[0]) == int(i):
                     checker2 += 1
             while checker2<1:
                 print("you choosed a number which is not found in the list please choose again wisely")
                 player2 = input(" player2 choose a token number ").split()
                 for i in tokens:
                     if int(player2[0]) == int(i):
                         checker2 += 1
             tokens.remove(int(player2[0]))
         if len(tokens) == 0:
             print("player 2 wins")
             break
 contin = input("do you want to play again enter yes or no")
 if contin=="yes":
     desscion1=1
 elif contin=="no":
     desscion1=0
 else:
     desscion1=2
 while desscion1==2:
     print("sorry wrong input please enter yes or no")
     contin = str(input("do you want to play again enter yes or no"))
     if contin == "yes":
         desscion1=1
     elif contin=="no":
         desscion1 = 0
     else:desscion1=2
 if desscion1 == 1:
     desscion=1
 else:
     print("thank you good bye")
     desscion=0

















