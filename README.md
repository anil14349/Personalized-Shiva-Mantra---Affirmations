# Personalized Shiva Mantra & Affirmations

A web application that generates personalized Shiva mantras and affirmations based on your name and purpose, powered by AI.

## Features

- Generate personalized Sanskrit mantras with pronunciation guides
- Get English translations and modern affirmations
- Listen to your mantra through text-to-speech
- Download your mantra in text and audio formats
- Beautiful, spiritual user interface

## Setup

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Technologies Used

- Streamlit - Web application framework
- OpenAI GPT - AI-powered mantra generation
- gTTS (Google Text-to-Speech) - Audio generation
- Python - Backend programming

## Usage

1. Enter your name
2. Select your purpose (e.g., peace, health, prosperity)
3. Click "Generate Mantra"
4. Listen to or download your personalized mantra

## Note

This application requires an OpenAI API key to function. Make sure to keep your API key secure and never share it publicly.
