
import speech_recognition as sr
import pyttsx3
import webbrowser
import os

r = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


speak("Hello sir, Jarvis is ready.")

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=5, phrase_time_limit=5)

        command = r.recognize_google(audio, language="en-IN").lower()
        print("You said:", command)

        if "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "open notepad" in command:
            speak("Opening Notepad")
            os.system("notepad.exe")

        elif "open calculator" in command:
            speak("Opening Calculator")
            os.system("calc.exe")

        elif "open chatgpt" in command:
            speak("Opening ChatGPT")
            webbrowser.open("https://chatgpt.com")
  

        elif "stop jarvis" in command or "exit" in command:
            speak("Goodbye sir")
            break

        else:
            speak("Sorry sir, command not found.")

    except sr.WaitTimeoutError:
        continue

    except sr.UnknownValueError:
        speak("Sorry sir, please repeat.")

    except sr.RequestError:
        speak("Internet connection problem.")

    except Exception as e:
        print("Error:", e)
