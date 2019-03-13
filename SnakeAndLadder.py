def nxt(val,n,lis):
    val=val+n-1 #adding the current player sate and dice value to get next sate
    if (val<10):
        i=0
        j=val
    else:
        j=val%10
        i=int((val)/10)
    print(i,j)
    return lis[i][j] #it return current player stage

#main function execution stares here
lis=[] #empty list for the board
count=0
for i in range(1,11): # board is considered as a tow dimensional array
    l=[]
    for j in range(1,11):
        count+=1
        l.append(count)
    lis.append(l)

#ladder
lis[0][3]=77
lis[1][6]=29
lis[2][4]=94
lis[4][7]=62
lis[6][3]=79

#snake
lis[9][5]=20
lis[7][1]=71
lis[3][2]=32
lis[5][0]=40

#initial board printing after the snake and ladder adding
for i in lis:
    for j in i:
        print(j,end="\t")
    print()
    
    
#intial condition for loop maintanace and player current state    
playerWin=True
current=1


while(playerWin):
    if(current>99):
        print("You Won.....!!")
        playerWin=False
    else:
        n=int(input("You are at : "+str(current)+"\nEnter the value :"))#getting value from the user 
        n=(n%5)+1  #dice containes only 6 moves
        current=nxt(current,n,lis)#function calll
        
        
    

