from tkinter import *
import webbrowser
import cv2
from cvzone.HandTrackingModule import HandDetector
import random
from PIL import ImageTk, Image

#Functions
#Open my Website in Browser
def openWebsite(url):
    webbrowser.open_new(url)
#Defining Result Window
def resultWindow(yr_choice, dev_choice, result):
    your_choice = Label(win, text="Your Choice:", font=("Times", "20", "underline"), fg="blue", bg="lemon chiffon")
    your_choice.pack()
    your_choice.place(x=65, y=65)
    device_choice = Label(win, text="Device's Choice:", font=("Times", "20", "underline"), fg="blue", bg="lemon chiffon")
    device_choice.pack()
    device_choice.place(x=490, y=65)
    paper_path = "paper.jpg"
    rock_path = "rock.jpg"
    scissor_path = "scissor.jpg"
    if str(yr_choice) == "Paper":
        path = paper_path
        image1 = Image.open(path)
        test = ImageTk.PhotoImage(image1)
        label1 = Label(image=test)
        label1.image = test
        label1.pack()
        label1.place(x=50, y=100)
    if str(yr_choice) == "Rock":
        path = rock_path
        image1 = Image.open(path)
        test = ImageTk.PhotoImage(image1)
        label1 = Label(image=test)
        label1.image = test
        label1.pack()
        label1.place(x=50, y=100)
    if str(yr_choice) == "Scissor":
        path = scissor_path
        image1 = Image.open(path)
        test = ImageTk.PhotoImage(image1)
        label1 = Label(image=test)
        label1.image = test
        label1.pack()
        label1.place(x=50, y=100)
    if str(dev_choice) == "Paper":
        path = paper_path
        image1 = Image.open(path)
        test = ImageTk.PhotoImage(image1)
        label1 = Label(image=test)
        label1.image = test
        label1.pack()
        label1.place(x=485, y=100)
    if str(dev_choice) == "Rock":
        path = rock_path
        image1 = Image.open(path)
        test = ImageTk.PhotoImage(image1)
        label1 = Label(image=test)
        label1.image = test
        label1.pack()
        label1.place(x=485, y=100)
    if str(dev_choice) == "Scissor":
        path = scissor_path
        image1 = Image.open(path)
        test = ImageTk.PhotoImage(image1)
        label1 = Label(image=test)
        label1.image = test
        label1.pack()
        label1.place(x=485, y=100)
    canvas = Canvas(win,height=40,width=137,bg="#fff")
    canvas.pack()
    canvas.place(x=322, y=347)
    final_result = Label(win, text=result, font=("Times", "20"), fg="tomato", bg="lemon chiffon")
    final_result.pack()
    final_result.place(x=300, y=350)
#Create Game Window
def startGame():
    cap = cv2.VideoCapture(0)
    cap.set(3, 1000)
    cap.set(4, 640)
    detector = HandDetector(detectionCon=0.8)
    final = []
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList, bboxInfo = detector.findPosition(img)
        cv2.imshow("Image", img)
        # Check for Choices
        if lmList:
            choices = ["Rock", "Paper", "Scissor"]
            comp_choice = random.choice(choices)
            fingers = detector.fingersUp()
            thumbFinger = fingers[0]
            indexFinger = fingers[1]
            midFinger = fingers[2]
            ringFinger = fingers[3]
            lastFinger = fingers[4]
            if str(thumbFinger) == "0" and str(indexFinger) == "0" and str(midFinger) == "0" and str(
                    ringFinger) == "0" and str(lastFinger) == "0":
                #print("Your choice is Rock")
                #print(f"Computer's Choice is {comp_choice}")
                user_choice = "Rock"
                if str(user_choice) == str(comp_choice):
                    #print("Game Draw")
                    final.append("Game Draw")
                else:
                    if str(comp_choice) == "Paper":
                        #print("You Loose")
                        final.append("You Loose")
                    if str(comp_choice) == "Scissor":
                        #print("You Win")
                        final.append("You Win")
                resultWindow(user_choice, comp_choice, final[0])
                break
            if str(thumbFinger) == "1" and str(indexFinger) == "1" and str(midFinger) == "1" and str(
                    ringFinger) == "1" and str(lastFinger) == "1":
                #print("Your choice is Paper")
                #print(f"Computer's Choice is {comp_choice}")
                user_choice = "Paper"
                if str(user_choice) == str(comp_choice):
                    #print("Game Draw")
                    final.append("Game Draw")
                else:
                    if str(comp_choice) == "Rock":
                        #print("You Win")
                        final.append("You Win")
                    if str(comp_choice) == "Scissor":
                        #print("You Loose")
                        final.append("You Loose")
                resultWindow(user_choice, comp_choice, final[0])
                break
            if str(thumbFinger) == "0" and str(indexFinger) == "1" and str(midFinger) == "1" and str(
                    ringFinger) == "0" and str(lastFinger) == "0":
                #print("Your choice is Scissor")
                #print(f"Computer's Choice is {comp_choice}")
                user_choice = "Scissor"
                if str(user_choice) == str(comp_choice):
                    #print("Game Draw")
                    final.append("Game Draw")
                else:
                    if str(comp_choice) == "Paper":
                        #print("You Win")
                        final.append("You Win")
                    if str(comp_choice) == "Rock":
                        #print("You Loose")
                        final.append("You Loose")
                resultWindow(user_choice, comp_choice, final[0])
                break
        k = cv2.waitKey(1) & 0xFF
        # press 'q' to exit
        if k == ord('q'):
            cv2.destroyAllWindows()
            break

win = Tk()
win.geometry('720x500')
win.title("AI Rock Paper Scissor's Game")
win.configure(bg='lemon chiffon')
win.resizable(False, False)
win.iconbitmap('Brand-Logo-Icon.ico')
#App Name
appLabel = Label(win, text="AI Rock Paper Scissor's Game", font=("Times", "35", "bold italic"), fg="red", bg='lemon chiffon', anchor=CENTER) #Label for Appname
appLabel.pack() #Packs appLabel
appLabel.place(x=50,y=5) #Position for appLabel
#Start Button
start_button = Button(win, text="Start Game", fg='white', bg='red', font=("Helvetica", "15", "italic"), bd='3',  command=startGame) #Creates Add Contact Button
start_button.place(x=310,y=175) #Position add_button
#DEVELOPER LABEL
devNameLabel = Label(win, text="Developed By:", font=("Times", "20", "underline"), fg="green", bg="lemon chiffon")
devNameLabel.pack()
devNameLabel.place(x=200, y=400)
devName = Label(win, text="Raunak Kumar", font=("Times", "20"), fg="orange", bg="lemon chiffon")
devName.pack()
devName.place(x=375, y=400)
devContact = Label(win, text="Lets Connect", fg="blue", cursor="hand2")
devContact.pack()
devContact.place(x=200, y=440)
devContact.bind("<Button-1>", lambda e: openWebsite("https://www.raunakmishra.com.np/#Contact"))
win.mainloop()
