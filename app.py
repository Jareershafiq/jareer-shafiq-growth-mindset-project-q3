import streamlit as st
import pandas as pd
from streamlit_extras.add_vertical_space import add_vertical_space

# Set Page Config
st.set_page_config(page_title='Growth Mindset Hub', layout='wide', initial_sidebar_state='expanded')

# Custom CSS for Enhanced Gradient and Vibrant UI
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            color: white;
            font-family: 'Poppins', sans-serif;
        }
        .main-header {
            font-size: 3em;
            font-weight: bold;
            text-align: center;
            background: linear-gradient(90deg, #ff9a9e, #fad0c4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px;
        }
        .sub-header {
            font-size: 1.7em;
            color: #ffdd57;
            text-align: center;
            margin-bottom: 20px;
        }
        .footer {
            text-align: center;
            font-size: 1.5em;
            font-weight: bold;
            margin-top: 30px;
            color: #ffdd57;
        }
        .stButton>button {
            background: linear-gradient(90deg, #ff9a9e, #fad0c4);
            border: none;
            color: white;
            font-size: 1.2em;
            padding: 12px 24px;
            border-radius: 12px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #fad0c4, #ff9a9e);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown("<h1 class='main-header'>🚀 Growth Mindset Hub</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='sub-header'>Transform Your Mindset, Elevate Your Life</h2>", unsafe_allow_html=True)

# User Input Section
st.subheader("📝 Daily Growth Tracker")
name = st.text_input("Enter Your Name", "Guest")
age = st.number_input("Enter Your Age", min_value=10, max_value=100, step=1)
profession = st.text_input("Enter Your Profession")

if st.button("Let's Begin 🚀"):
    st.session_state['started'] = True

if 'started' in st.session_state:
    st.subheader("How are you feeling today?")
    feelings = st.multiselect("Select your current feelings:", ["Happy", "Sad", "Stressed", "Tired"])
    
    if "Happy" in feelings:
        st.success("Happiness is contagious! Keep spreading positivity! 😊")
    if "Sad" in feelings:
        st.warning("Tough times don't last, but tough people do. Stay strong! 💪")
    if "Stressed" in feelings:
        st.info("Breathe in, breathe out. You're capable of handling this! 🌿")
    if "Tired" in feelings:
        st.error("Rest is important. Recharge and come back stronger! 🔋")
    
    st.subheader("⚡ Energy Level Tracker")
    energy_level = st.slider("Rate your energy level for today:", 0, 100, 50)
    st.write(f"Your energy level is: {energy_level}")
    
    st.subheader("🏆 Daily Challenges & Tasks")
    challenge = st.text_area("Set your daily challenge:")
    if st.button("Save Challenge"):
        st.session_state['challenge'] = challenge
    
    if 'challenge' in st.session_state:
        st.write("### Your Challenge:")
        st.write(st.session_state['challenge'])
    
    st.subheader("📖 Mindfulness Exercises")
    if st.button("Start Breathing Exercise"):
        st.write("Breathe in... Hold... Breathe out...")
    
    st.subheader("✅ Habit Tracker")
    habit_options = ["Read a book", "Meditate", "Drink Water", "Journal Writing"]
    selected_habits = {}
    
    for habit in habit_options:
        selected_habits[habit] = st.checkbox(habit)
    
    quotes = {
        "Read a book": "A reader lives a thousand lives before he dies. 📖",
        "Meditate": "Quiet the mind, and the soul will speak. 🧘‍♂️",
        "Drink Water": "Stay hydrated, stay healthy! 💧",
        "Journal Writing": "Fill your paper with the breathings of your heart. ✍️"
    }
    
    for habit, selected in selected_habits.items():
        if selected:
            st.write(f"**{habit}** - {quotes[habit]}")
    
    st.sidebar.subheader("User Profile")
    st.sidebar.write(f"**Name:** {name}")
    st.sidebar.write(f"**Age:** {age}")
    st.sidebar.write(f"**Profession:** {profession}")
    
    st.markdown("<div class='footer'>Remember: Small steps lead to big changes. Keep pushing forward! 🌟</div>", unsafe_allow_html=True)
    
st.markdown("<div class='footer'>Made by Jareer Shafiq</div>", unsafe_allow_html=True)
