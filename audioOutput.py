import pyttsx3


def test():
    input = "hello test "
    engine = pyttsx3.init()
    # voices = engine.getProperty('voices')
    rate = 150
    print(rate)

    engine.setProperty('rate', rate)
    volume = engine.getProperty('volume')
    print(volume)

    engine.setProperty('volume', volume)
    engine.say(input)
    engine.runAndWait()


def speak(input, rate=150):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)

    engine.say(input)
    engine.runAndWait()


if __name__ == '__main__':
    text = 'hello, today is thursday!'
    print('speak')
    speak(text)
