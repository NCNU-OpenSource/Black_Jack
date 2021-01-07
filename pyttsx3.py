import pyttsx3
input = "hello test "
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = 150
print(rate)
engine.setProperty('rate', rate)
volume = engine.getProperty('volume')
print(volume)
engine.setProperty('volume', volume)
engine.say(input)
engine.runAndWait()