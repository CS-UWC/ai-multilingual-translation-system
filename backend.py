from flask import Flask, render_template, request
from flask_socketio import SocketIO
from deep_translator import GoogleTranslator

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

translation_cache = {}

@app.route('/')
def lecturer():
    return render_template('lecturer.html')

@app.route('/student')
def student():
    return render_template('student.html')

@socketio.on('send_text')
def handle_text(data):
    text =data['text'].strip()
    if not text:
        return
    socketio.emit('process_translation', {'english': text})

@socketio.on('request_translation')
def translate_per_student(data):
    text = data['text']
    lang= data['language']
    cache_key= f"{text}-{lang}"

    if cache_key in translation_cache:
        translated = translation_cache[cache_key]
    else:
        try:
            translated = GoogleTranslator(source='en', target=lang).translate(text)
            translation_cache[cache_key] = translated
        except Exception as e:
            translated = "[Translation Timeout]"
            print(f"Error translating to {lang}: {e}")

    socketio.emit('receive_translation', {
        'english': text,
        'translated': translated
    }, to=request.sid)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
