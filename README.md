# customer-service-bot
# 🎙️ Voice-Based Customer Service Bot

This is a voice-interactive customer service bot built using Python. It listens to user queries via microphone input, understands spoken commands, and responds with speech using text-to-speech (TTS). The bot simulates a basic customer service assistant capable of answering common support questions and guiding users.

---

## 🧠 Features

- 🎤 Speech recognition using Google Web Speech API
- 🗣️ Voice response using `pyttsx3` (offline TTS engine)
- 🧾 Understands basic customer service queries like:
  - Order tracking
  - Product information
  - Return/refund policy
  - Support connection
- 🆘 Help command to list available options
- 🚪 Graceful exit on "bye", "exit", or "quit"

---

## 🛠️ Technologies Used

- `speech_recognition` for converting speech to text
- `pyttsx3` for converting text to speech (TTS)
- `Python` standard libraries

---

## 📁 Project Structure




---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/customer-service-bot.git
cd customer-service-bot

python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

pip install speechrecognition pyttsx3 pyaudio


python app.py



