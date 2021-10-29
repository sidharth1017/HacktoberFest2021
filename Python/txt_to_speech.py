#import the packages
import pyttsx3
engine = pyttsx3.init()
#ask for the the text
engine.say(input('> Type yout text here: '))
engine.runAndWait()