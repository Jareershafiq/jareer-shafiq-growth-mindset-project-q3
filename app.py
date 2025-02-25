import streamlit as st
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

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
