import pyttsx3
engine = pyttsx3.init()

# Voice IDs pulled from engine.getProperty('voices')
# These will be system specific
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"

# Use female English voice
engine.setProperty('voice', en_voice_id)
engine.say('Hello with my new voice')

# Use female Russian voice
engine.setProperty('voice', ru_voice_id)
engine.say('Привет. где хакер')

engine.runAndWait()