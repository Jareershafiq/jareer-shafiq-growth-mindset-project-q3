import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os

def speak(text):
    """Convert text to speech using gTTS"""
    tts = gTTS(text=text, lang="en")
    tts.save("welcome.mp3")
    st.audio("welcome.mp3", autoplay=True)

def recognize_speech():
    """Recognize speech from microphone"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            return command.lower()
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand."
        except sr.RequestError:
            return "Speech Recognition service is unavailable."

# Streamlit UI
st.title("Voice Assistant in Streamlit")

# Welcome message when app starts
welcome_text = "Welcome to Growth Mindset App made by Jareer Shafiq."
st.write(f"🎙 {welcome_text}")
speak(welcome_text)  # Speak the welcome message

# Button to start voice recognition
if st.button("🎤 Speak"):
    user_input = recognize_speech()
    st.write(f"**You said:** {user_input}")
    speak(f"You said: {user_input}")
    
    # Process commands
    if "weather" in user_input:
        response = "Checking the weather for you!"
    elif "hello" in user_input:
        response = "Hello! How can I assist you today?"
    else:
        response = "I am not sure how to respond to that."

    st.write(f"**Assistant:** {response}")
    speak(response)
