from  tkinter import *
import  random
n=52
def gen_pocker(n):
    x=100
    while(x>0):
        x=x-1
        p1=random.randint(0,n-1)
        p2=random.randint(0,n-1)
        t=pocker[p1]
        pocker[p1]=pocker[p2]
        pocker[p2]=t
    return pocker

pocker=[i for i in range(n)]
pocker=gen_pocker(n)
print(pocker)

(player1,player2,player3,player4)=([],[],[],[])
(p1,p2,p3,p4)=([],[],[],[])
root=Tk()
cv=Canvas(root,bg='white',width=700,height=600)
imgs=[]
for i in range(1,5):
    for j in range(1,14):
        imgs.insert((i-1)*13+(j-1),PhotoImage(file='images\\'+str(i)+'-'+str(j)+'.gif'))
for x in range(13):
    m=x*4
    p1.append(pocker[m])
    p2.append(pocker[m+1])
    p3.append(pocker[m+2])
    p4.append(pocker[m+3])
p1.sort()
p2.sort()
p3.sort()
p4.sort()
for x in range(0,13):
    img=imgs[p1[x]]
    player1.append(cv.create_image((200+20*x,80),image=img))
    img = imgs[p2[x]]
    player2.append(cv.create_image((100,150+20*x),image=img))
    img = imgs[p3[x]]
    player3.append(cv.create_image((200+20*x,500),image=img))
    img = imgs[p4[x]]
    player4.append(cv.create_image((560,150+20*x),image=img))
print("player1:",player1)
print("player2:",player2)
print("player3:",player3)
print("player4:",player4)
cv.pack()
root.mainloop()
print("Done")
