import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0)  # to capture video

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

prevTime = 0
currTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks) # will notify/print when a hand appears in front of camera

    # to check if we have multiple hands or not
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                if id == 4:
                    cv.circle(img, (cx, cy), 15, (255, 0, 255), cv.FILLED)   # will circle the point whose id is 4

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)     # will draw dots on hand and connects them

    currTime = time.time()  # gives current time
    fps = 1/(currTime-prevTime)
    prevTime = currTime

    cv.putText(img, str(int(fps)), (10,70), cv.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

    cv.imshow('Image', img)
    cv.waitKey(1)
