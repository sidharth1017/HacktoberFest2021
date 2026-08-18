import tkinter as tk
from tkinter import*
import tkinter.font as font
import random
root=Tk()
root.title('TIC TAC TOE')
root.geometry('300x150')
myFont = font.Font(family='Helvetica', size=15, weight='bold')
player_choice=Label(root,text="-::CHOOSE YOUR PLAYER::- ",font=myFont,width=23,borderwidth=10).grid(row=0,columnspan=2)
pl=['X','O']
def player(a):
    if(a=='O'):
        pl[0]='O';pl[1]='X'
    l=Label(root,text='Selected, Click the ✕ button',font=myFont,borderwidth=10).grid(row=2,columnspan=2)
    
X=Button(root,text='✕',font=myFont,padx=15,pady=10,command=lambda: player('X')).grid(row=1,column=0)
Y=Button(root,text='O',font=myFont,padx=15,pady=10,command=lambda: player('O')).grid(row=1,column=1)

root.mainloop()
  
root=Tk()

root.title('TIC TAC TOE')
root.geometry('405x300')

myFont = font.Font(family='Helvetica', size=15, weight='bold')

toss=Label(root,text="-::TOSS::-\nSELECT CHOICE",font=myFont,width=30,borderwidth=10).grid(row=0,columnspan=2)
tw=[1]
def toss(ts):
    a=random.randint(0,1)
    if(a==1):
        tx='IT IS HEAD'
    else:
        tx='IT IS TAIL'
    l=Label(root,text=tx,font=myFont,borderwidth=10).grid(row=2,columnspan=2)
    if(ts==a):
        tx='YOU WON THE TOSS\nYOU WILL GIVE THE TURN FIRST\nClick the ✕ button to start the game'
    else:
        tw[0]=0
        tx='COMPUTER WON THE TOSS\nCOMPUTER WILL GIVE THE TURN FIRST\nClick the ✕ button to start the game'
    l=Label(root,text=tx,font=myFont,borderwidth=10).grid(row=3,columnspan=2)

H=Button(root,text='HEAD',font=myFont,padx=15,pady=10,command=lambda: toss(1)).grid(row=1,column=0)
T=Button(root,text='TAIL',font=myFont,padx=15,pady=10,command=lambda: toss(0)).grid(row=1,column=1)

root.mainloop()


root=Tk()
root.title("TIC TAC TOE")
root.geometry('360x640')

myFont = font.Font(family='Helvetica', size=12,weight='bold')

score=Label(root,text='SCOREBOARD',width=10,font=myFont,borderwidth=7).grid(row=0,columnspan=3)

myFont = font.Font(family='Helvetica', size=9,weight='bold')

youL=Label(root,text='YOU',width=9,font=myFont,borderwidth=5).grid(row=1,column=0)
youE=Entry(root,width=5,borderwidth=5)
youE.grid(row=2,column=0)
youE.insert(-1,'0')

compL=Label(root,text='COMPUTER',width=9,font=myFont,borderwidth=5).grid(row=1,column=1)
compE=Entry(root,width=5,borderwidth=5)
compE.grid(row=2,column=1)
compE.insert(-1,'0')

drawL=Label(root,text='DRAW',width=9,font=myFont,borderwidth=5).grid(row=1,column=2)
drawE=Entry(root,width=5,borderwidth=5)
drawE.grid(row=2,column=2)
drawE.insert(-1,'0')

myFont = font.Font(family='Helvetica', size=12, weight='bold')

board=Label(root,text='GAMEBOARD',width=10,font=myFont,borderwidth=7).grid(row=4,columnspan=3)

myFont = font.Font(family='Helvetica', size=20,weight='bold')  

t=[]
pos=['1','2','3','4','5','6','7','8','9']
m=pl[0];c=pl[1]
scores=[0,0,0]
buttons=[]

btx1=tk.StringVar()
btx2=tk.StringVar()
btx3=tk.StringVar()
btx4=tk.StringVar()
btx5=tk.StringVar()
btx6=tk.StringVar()
btx7=tk.StringVar()
btx8=tk.StringVar()
btx9=tk.StringVar()

btx1.set('   ')
btx2.set('   ')
btx3.set('   ')
btx4.set('   ') 
btx5.set('   ')
btx6.set('   ')
btx7.set('   ')
btx8.set('   ')
btx9.set('   ')

btx=[btx1,btx2,btx3,btx4,btx5,btx6,btx7,btx8,btx9]

t=[['1','2','3'],['4','5','6'],['7','8','9']]
    
global b_1,b_2,b_3,b_4,b_5,b_6,b_7,b_8,b_9

b_1=Button(root,textvariable=btx1,bg='#FFFF88',font=myFont,command=lambda: game_turn(1),padx=34,pady=30)
b_2=Button(root,textvariable=btx2,bg='#FFFF88',font=myFont,command=lambda: game_turn(2),padx=35,pady=30)
b_3=Button(root,textvariable=btx3,bg='#FFFF88',font=myFont,command=lambda: game_turn(3),padx=35,pady=30)
b_4=Button(root,textvariable=btx4,bg='#FFFF88',font=myFont,command=lambda: game_turn(4),padx=35,pady=30)
b_5=Button(root,textvariable=btx5,bg='#FFFF88',font=myFont,command=lambda: game_turn(5),padx=35,pady=30)
b_6=Button(root,textvariable=btx6,bg='#FFFF88',font=myFont,command=lambda: game_turn(6),padx=35,pady=30)
b_7=Button(root,textvariable=btx7,bg='#FFFF88',font=myFont,command=lambda: game_turn(7),padx=35,pady=30)
b_8=Button(root,textvariable=btx8,bg='#FFFF88',font=myFont,command=lambda: game_turn(8),padx=35,pady=30)
b_9=Button(root,textvariable=btx9,bg='#FFFF88',font=myFont,command=lambda: game_turn(9),padx=35,pady=30)

b_1.grid(row=5,column=0)
b_2.grid(row=5,column=1)
b_3.grid(row=5,column=2)
b_4.grid(row=6,column=0)
b_5.grid(row=6,column=1)
b_6.grid(row=6,column=2)
b_7.grid(row=7,column=0)
b_8.grid(row=7,column=1)
b_9.grid(row=7,column=2)

buttons=[b_1,b_2,b_3,b_4,b_5,b_6,b_7,b_8,b_9]

btns=[[b_1,b_2,b_3],[b_4,b_5,b_6],[b_7,b_8,b_9]]

blank=Label(root,width=50).grid(row=8,columnspan=3)
result=Entry(root,width=50,borderwidth=5)
result.grid(row=9,columnspan=3)

myFont = font.Font(family='Helvetica', size=12, weight='bold')

play_again=Label(root,text='Do You Want To Play Again?',font=myFont,width=22,borderwidth=7).grid(row=10,columnspan=3)

myFont = font.Font(family='Helvetica', size=8,weight='bold')

yes=Button(root,text='YES',font=myFont,command=lambda: yesf(),padx=15,pady=10)
yes.grid(row=11,column=0,columnspan=1)
yes['state']=DISABLED

no=Button(root,text='NO',font=myFont,command=lambda: nof(),padx=15,pady=10)
no.grid(row=11,column=2,columnspan=1)
no['state']=DISABLED

restart=Button(root,text='Restart',font=myFont,command=lambda: resf(),padx=20,pady=10)
restart.grid(row=12,columnspan=3)
restart['state']=DISABLED

def yesf():
    t[0]=['1','2','3']
    t[1]=['4','5','6']
    t[2]=['7','8','9']
    for i in range(9):
        buttons[i]['bg']='#FFFF88'
        btx[i].set('   ')
        buttons[i]['state']=ACTIVE
    yes['state']=DISABLED
    no['state']=DISABLED
    restart['state']=DISABLED
    result.delete(0,END)
    if(tw[0]==0):
        game_board(computer_turn(),c)
    
def nof():
    root.destroy()
    
def resf():
    scores[0]=0;scores[1]=0;scores[2]=0
    youE.delete(0,END)
    youE.insert(-1,str(scores[0]))
    compE.delete(0,END)
    compE.insert(-1,str(scores[1]))
    drawE.delete(0,END)
    drawE.insert(-1,str(scores[2]))
    t[0]=['1','2','3']
    t[1]=['4','5','6']
    t[2]=['7','8','9']
    for i in range(9):
        buttons[i]['bg']='#FFFF88'
        btx[i].set('   ')
        buttons[i]['state']=ACTIVE
    yes['state']=DISABLED
    no['state']=DISABLED
    restart['state']=DISABLED
    result.delete(0,END)
    if(tw[0]==0):
        game_board(computer_turn(),c)

def game_executer():
    game=0
    for k in range(3):
        if((t[k][0]==t[k][1] and t[k][1]==t[k][2]) or
           (t[0][k]==t[1][k] and t[1][k]==t[2][k])):
            game=1
            if(t[k][0]==t[k][1] and t[k][1]==t[k][2]):
                btns[k][0]['bg']='#ADD8E6'
                btns[k][1]['bg']='#ADD8E6'
                btns[k][2]['bg']='#ADD8E6'
            else:
                btns[0][k]['bg']='#ADD8E6'
                btns[1][k]['bg']='#ADD8E6'
                btns[2][k]['bg']='#ADD8E6'
            break
    if(game==0):
        if((t[0][0]==t[1][1] and t[1][1]==t[2][2]) or 
           (t[0][2]==t[1][1] and t[1][1]==t[2][0])):
            game=1
            if(t[0][0]==t[1][1] and t[1][1]==t[2][2]):
                btns[0][0]['bg']='#ADD8E6'
                btns[1][1]['bg']='#ADD8E6'
                btns[2][2]['bg']='#ADD8E6'
            else:
                btns[0][2]['bg']='#ADD8E6'
                btns[1][1]['bg']='#ADD8E6'
                btns[2][0]['bg']='#ADD8E6'
    if(game==0):
        game=-1
        for i in t:
            for j in i:
                if j in pos:
                    game=0
                    break
    return game
def computer_turn():
    turn=0
    """searching winning scope"""
    for k in range(3):
        hor=sorted(t[k])
        ver=sorted([t[0][k],t[1][k],t[2][k]])
        if(hor[0] in pos and hor[1]==c and hor[2]==c):
            turn=hor[0]
            break
        if(ver[0] in pos and ver[1]==c and ver[2]==c):
            turn=ver[0]
            break
    if(turn==0):
        d1=sorted([t[0][0],t[1][1],t[2][2]])
        d2=sorted([t[0][2],t[1][1],t[2][0]])
        if(d1[0] in pos and d1[1]==c and d1[2]==c):
            turn=d1[0]
        elif(d2[0] in pos and d2[1]==c and d2[2]==c):
            turn=d2[0]
    """defensive"""
    if(turn==0):
        for k in range(3):
            hor=sorted(t[k])
            ver=sorted([t[0][k],t[1][k],t[2][k]])
            if(hor[0] in pos and hor[1]==m and hor[2]==m):
                turn=hor[0]
                break
            if(ver[0] in pos and ver[1]==m and ver[2]==m):
                turn=ver[0]
                break
        if(turn==0):
            d1=sorted([t[0][0],t[1][1],t[2][2]])
            d2=sorted([t[0][2],t[1][1],t[2][0]])
            if(d1[0] in pos and d1[1]==m and d1[2]==m):
                turn=d1[0]
            elif(d2[0] in pos and d2[1]==m and d2[2]==m):
                turn=d2[0]
    """offensive"""
    if(turn==0):
        for k in range(3):
            hor=sorted(t[k])
            ver=sorted([t[0][k],t[1][k],t[2][k]])
            if(hor[0] in pos and hor[1] in pos and hor[2]==m):
                turn=random.choice([hor[0],hor[1]])
                break
            if(ver[0] in pos and ver[1] in pos and ver[2]==m):
                turn=random.choice([ver[0],ver[1]])
                break
        if(turn==0):
            d1=sorted([t[0][0],t[1][1],t[2][2]])
            d2=sorted([t[0][2],t[1][1],t[2][0]])
            if(d1[0] in pos and d1[1] in pos and d1[2]==m):
                turn=random.choice([d1[0],d1[1]])
            elif(d2[0] in pos and d2[1] in pos and d2[2]==m):
                turn=random.choice([d2[0],d2[1]])
    """random"""
    if(turn==0):
        while(1):
            i=random.randint(0,2)
            j=random.randint(0,2)
            if t[i][j] in pos:
                turn=t[i][j]
                break
    return turn

def game_board(n,pl):
    for i in range(3):
        for j in range(3):
            if(t[i][j]==n): t[i][j]=pl;break
    if(pl=='X'):
        btx[int(n)-1].set('✕')
    if(pl=='O'):
        btx[int(n)-1].set('O')
    buttons[int(n)-1]['state']=DISABLED

def button_mode():
    for i in range(9):
        buttons[i]['state']=DISABLED
    yes['state']=ACTIVE
    no['state']=ACTIVE
    restart['state']=ACTIVE
    
if(tw[0]==0):
    game_board(computer_turn(),c)
    
def game_turn(n):
    game_board(str(n),m)
    if(game_executer()==1):  
        result.insert(0,'\t\t  YOU WON!!!')
        scores[0]+=1
        youE.delete(0,END)
        youE.insert(-1,str(scores[0]))
        button_mode()
        return
    elif(game_executer()==-1): 
        result.insert(0,'\t\t  GAME DRAWN')
        scores[2]+=1
        drawE.delete(0,END)
        drawE.insert(-1,str(scores[2]))
        button_mode()
        return
    game_board(computer_turn(),c)
    if(game_executer()==1):
        result.insert(0,'\t\t  COMPUTER WON')
        scores[1]+=1
        compE.delete(0,END)
        compE.insert(-1,str(scores[1]))
        button_mode()
        return
    elif(game_executer()==-1): 
        result.insert(0,'\t\t  GAME DRAWN')
        scores[2]+=1
        drawE.delete(0,END)
        drawE.insert(-1,str(scores[2]))
        button_mode()
        return
    
root.mainloop()


    


    






