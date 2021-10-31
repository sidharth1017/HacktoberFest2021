from tkinter import *
import random

#list of possible colour. 
colours = ['Red','Blue','Green','Pink','Black', 
           'Yellow','Orange','White','Purple','Brown']
score  = 0
#To take in account the time left: initially 30 seconds
time = 30

#Function that will start the Game
def startGame(event):

    if time==30:

        #start the countdown timer
        countdown()
    nextcolor()

def nextcolor():

    global score
    global time

    #if a game is in play
    if time > 0:

        #make the text entry box active
        colour_entry.focus_set()

        if colour_entry.get().lower() == colours[1].lower():

            score += 1

        #clear the entry the box 
        colour_entry.delete(0, END)

        random.shuffle(colours) 

        # change the colour to type, by changing the 
        # text _and_ the colour to a random colour value
        colour.config(fg= str(colours[1]) , text = str(colours[0]))

        # update the score. 
        scoreLabel.config(text = "Score: " + str(score))

#Countdown Timer Fuction
def countdown():

    global time

    #if a game is in play
    if time > 0 :

        #decrement the value
        time -= 1

        # update the time left label 
        timeLabel.config(text = "Time left: "+ str(time))

        # run the function again after 1 second. 
        timeLabel.after(1000, countdown)

#Driver Code
if __name__=='__main__':

    root = Tk()

    #Setting the title 
    root.title('Color Game') 

    #Setting the geometry of the window
    root.geometry('375x200')

    #set an instruction label 
    instructions = Label(root, text = 'Type in the colour of the words, and not the word text!', font = ('Helvetica', 12)) 
    instructions.pack()

    #Create a Score label
    scoreLabel = Label(root, text = 'Score :'+str(score), font=('Helvetica' , 12))
    scoreLabel.pack()

    #Create a Time Label 
    timeLabel = Label(root, text = 'Time Left : '+str(time), font=('Helvetica' , 12))
    timeLabel.pack()

    #create a colour label
    colour = Label(root, font=('Helevetica',12))
    colour.pack()

    #Entry box for input from user
    colour_entry = Entry(root)


    colour_entry.focus_set()
    root.bind('<Return>',startGame)

    colour_entry.pack()

    root.mainloop()
