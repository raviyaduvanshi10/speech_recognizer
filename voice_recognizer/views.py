from django.shortcuts import render
from django.shortcuts import render
import speech_recognition as sr


def voice_form(request):
    print("Please tell your name ...")
    name = voice_recording()
    print("Please tell your job position ...")
    job = voice_recording()
    print("Please tell your city ...")
    city = voice_recording()
    print("Please tell your state ...")
    state = voice_recording()
    print("Please tell your country ...")
    country = voice_recording()
    print("Submitting the data ...")
    data = { "Name": name, "Job Role": job, "City": city, "State": state, "Country":country}
    return render(request, 'voice_recognizer/index.html', {"data": data})


def voice_recording():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening Text ...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing Text ...")
        text = recognizer.recognize_google(audio)
        print(text)
        return text
    except sr.UnknownValueError:
        print("Could not able to listen!")
    except sr.RequestError as e:
        print("results; {0}".format(e))