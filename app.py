import streamlit as st
from gtts import gTTS
import os
import base64
import tempfile
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Gemini API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Configure the model
model = genai.GenerativeModel('gemini-2.0-flash')

def generate_mantra(name, purpose):
    """Generate personalized mantra using Google's Gemini model."""
    prompt = f"""Create a personalized Shiva mantra and affirmation for {name} who seeks {purpose}. 
    The response should include:
    1. A short Sanskrit mantra (with pronunciation guide)
    2. Its English translation
    3. A modern affirmation (2-3 sentences)
    
    Format the response clearly with appropriate line breaks between sections."""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error generating mantra: {str(e)}")
        return None

def text_to_speech(text, lang='en'):
    """Convert text to speech and return the audio file as base64."""
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
            tts = gTTS(text=text, lang=lang, slow=False)
            tts.save(fp.name)
            with open(fp.name, 'rb') as audio_file:
                audio_bytes = audio_file.read()
            os.unlink(fp.name)
            return base64.b64encode(audio_bytes).decode()
    except Exception as e:
        return None

# Set page config
st.set_page_config(
    page_title="Personalized Shiva Mantra & Affirmations",
    page_icon="🕉️",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(to bottom right, #1a1a2e, #16213e);
        color: white;
    }
    .stTextInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
    }
    .stSelectbox > div > div > select {
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.title("🕉️ Personalized Shiva Mantra & Affirmations")
st.markdown("*Harness the divine energy of Lord Shiva with personalized mantras and affirmations*")

# Input fields
name = st.text_input("Enter your name", placeholder="Your name")
purpose = st.selectbox(
    "Select your purpose",
    ["Inner Peace", "Spiritual Growth", "Health & Healing", "Strength & Courage", 
     "Wisdom & Knowledge", "Prosperity", "Protection", "Transformation"]
)

if st.button("Generate Mantra 🙏"):
    if name:
        with st.spinner("Generating your personalized mantra..."):
            mantra = generate_mantra(name, purpose)
            if mantra:
                st.markdown("### Your Personalized Mantra & Affirmation")
                st.markdown(mantra)
                
                # Generate audio
                audio_base64 = text_to_speech(mantra)
                if audio_base64:
                    st.markdown("### 🔊 Listen to Your Mantra")
                    st.markdown(f'<audio controls><source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3"></audio>', 
                              unsafe_allow_html=True)
                
                # Download buttons
                st.download_button(
                    label="Download Mantra Text",
                    data=mantra,
                    file_name=f"shiva_mantra_{name}.txt",
                    mime="text/plain"
                )
                
                if audio_base64:
                    st.download_button(
                        label="Download Audio",
                        data=base64.b64decode(audio_base64),
                        file_name=f"shiva_mantra_{name}.mp3",
                        mime="audio/mp3"
                    )
    else:
        st.error("Please enter your name to generate a personalized mantra.")

# Footer
st.markdown("---")
st.markdown(
    "Made with ❤️ and the blessings of Lord Shiva 🕉️"
)
