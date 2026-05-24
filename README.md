# 🌍 AI-Based Multilingual Lecture Translation System

A real-time AI-powered lecture translation platform designed to improve accessibility and inclusivity in higher education, specifically for first-year Computer Science students in South Africa. This system translates live lectures from English into **isiZulu, isiXhosa and Afrikaans** using AI-based Speech Recognition (ASR), Text To Speech (TTS) and Neural Machine Translation (NMT).

---

## 🚀 Overview

A large number of students in South African universities face a language barrier due to lectures being delivered in English, while majority of them do not have it as their first language. This system provides a solution by providing:

- 🎤 Real-time lecture speech capturing
- 🧠 AI-based text translation
- 💬 Live subtitles in multiple languages
- 🔊 Optional text-to-speech output
- 🌐 Web-based interface for students and lecturers

---

## 🧠 Key Features Of The System

### 🎧 Real-Time Lecture Processing
- Captures lecturer speech using browser microphone
- Streams live text to all connected students

### 🌍 Multilingual Translation
Supports:
- isiZulu (`zu`)
- isiXhosa (`xh`)
- Afrikaans (`af`)

### ⚡ Smart Caching System
- Reduces repeated API calls
- Improves translation speed and efficiency

### 🔊 Text-to-Speech (Optional)
- Converts translated text into natural speech
- Adjustable volume and speech rate

### 📡 Live System Status
- Displays real-time system state (Active / Idle)
- Connection feedback for users

---

## 🏗️ System Architecture

Lecturer Speech  
→ Browser Speech Recognition (ASR)  
→ Flask + Socket.IO Server  
→ GoogleTranslator (NMT)  
→ Translation Cache  
→ Student Interface  
→ Optional Speech Synthesis (TTS)

---

## 🧰 Tech Stack

### Backend
- Python 3
- Flask
- Flask-SocketIO
- deep-translator (GoogleTranslator)

### Frontend
- HTML5
- CSS3
- JavaScript
- Web Speech API (ASR + TTS)
- Socket.IO Client

---

## 📁 Project Structure

```text
project/
│
├── backend.py                 # Flask backend + Socket.IO logic
├── templates/
│   ├── lecturer.html      # Lecturer interface
│   └── student.html       # Student interface
│
└── README.md
```

## ⚙️ Installation

1. Clone repository:
```bash
git clone https://github.com/yourusername/multilingual-lecture-translator.git
cd multilingual-lecture-translator

2. Create virtual environment:
python -m venv venv

3. Activate:
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

4. Install dependencies:
pip install flask flask-socketio deep-translator
```

## ▶️ Run the Application
python backend.py
Then open in browser:

- Student Interface:
http://localhost:5000/student

- Lecturer Interface:
http://localhost:5000/

## 🔄 Socket Events
- send_text → Sends lecturer speech
- process_translation → Broadcasts English text
- request_translation → Requests translation per student
- receive_translation → Returns translated output

## 🧩 Backend Logic
- Flask-SocketIO handles real-time communication
- deep-translator performs neural machine translation
- Translation caching reduces API usage and improves efficiency
- Error handling ensures fallback responses if translation fails

## 🎓 Use Case

This system is designed for:
- First-year Computer Science students
- Multilingual classrooms
- Higher education accessibility solutions
- Real-time lecture assistance systems

## ⚠️ Limitations
- Supports only 3 South African languages
- Requires stable internet connection
- Limited handling of idioms and slang
- One-way communication (lecturer → student only)

## 🔮 Future Improvements
- Add all 12 official South African languages
- Enable bidirectional communication
- Integrate custom-trained NMT model
- Add lecture recording and playback
- Improve accuracy for technical Computer Science terminology

---
Advancing AI in Higher Education
