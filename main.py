import speech_recognition as spr

listener = spr.Recognizer()

try:

    with spr.Microphone() as source:
        listener.adjust_for_ambient_noise(source,5)
        audio = listener.listen(source)
        my_text = listener.recognize_google(audio)
        result = my_text.lower()

        if 'siri' in result:
            print(my_text)

        else:
            print('None')

except spr.UnknownValueError:
    print('Error occured')

