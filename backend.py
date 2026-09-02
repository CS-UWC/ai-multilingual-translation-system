
# 4261579
# Backend: Python

import os
from flask import Flask, request, jsonify, send_from_directory
from deep_translator import GoogleTranslator
from flask_cors import CORS

app =Flask(__name__, template_folder='.')
CORS(app)

UPLOAD_FOLDER = 'uploaded_media'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

lecture_data ={
    "current_text": "Waiting for the lecturer to begin speaking...",
    "is_broadcasting": False
}

language_codes={
    'zu':'zu',
    'xh':'xh',
    'af':'af',
    'en':'en'
}


translation_cache= {}

@app.route('/')
def web_interface():
    return send_from_directory('.','frontend.html')

@app.route('/process_lecture_text',methods=['POST'])
def process_lecture_text():
    data=request.json or {}
    new_text= data.get('text', '').strip()
    broadcast_status= data.get('active', None)

    if new_text:
        lecture_data["current_text"]=new_text
        translation_cache.clear()
    if broadcast_status is not None:
        lecture_data["is_broadcasting"] = broadcast_status
    return jsonify({"success": True})

@app.route('/process_translation',methods=['POST'])
def process_translation():
    data=request.json or {}
    target_language =data.get('lang', 'zu')
    original_text =lecture_data["current_text"]
    is_broadcasting =lecture_data["is_broadcasting"]

    if original_text in ["Waiting for the lecturer to begin speaking...", "Lecture paused."]:
        return jsonify({
            "original_text": original_text,
            "translated_text": "...",
            "is_broadcasting": is_broadcasting
        })

    
    cache_key=f"{original_text}_{target_language}"
    if cache_key in translation_cache:
        return jsonify({
            "original_text":original_text,
            "translated_text": translation_cache[cache_key],
            "is_broadcasting": is_broadcasting,
            "language":target_language,
            "is_cached" : True
        })

    try:
        language_code=language_codes.get(target_language, target_language)
        translated_text = GoogleTranslator(source='auto',target=language_code).translate(original_text)
        translation_cache[cache_key] =translated_text
        
        return jsonify({
            "original_text":original_text,
            "translated_text":translated_text,
            "is_broadcasting":is_broadcasting,
            "language": target_language,
            "is_cached": False
        })
    except Exception as error:
        print(f"[Error]: {error}")
        return jsonify({"error": "Translation failed"}),500


@app.route('/process_media',methods=['POST'])
def process_media():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    media_file=request.files['file']
    target_language =request.form.get('lang','zu')

    if media_file.filename=='':
        return jsonify({"error": "No file selected"}),400

    if media_file:
        file_path= os.path.join(UPLOAD_FOLDER,media_file.filename)
        media_file.save(file_path)
        lecture_content = [
            "Good morning everyone, and welcome back to the Computer Science core lecture series. Today we are diving deep into architectural performance bottlenecks, specifically looking at how multi-threaded execution models manage shared resource paradigms.",
            "When designing an enterprise-level application, you will inevitably run into concurrency issues where multiple execution threads attempt to read and write to a centralized memory space simultaneously.",
            "To stop data corruption, we introduce mutual exclusion protocols, or mutex locks. However, over-synchronization can cripple system throughput, leading to thread starvation or critical deadlocks where processors sit completely idle.",
            "As software developers, your task is to strike a perfect balance between thread safety and high-performance computing streams. Let us map out the data structures required to optimize this network layer.",
            "Moving on to our secondary topic for the day: memory management and horizontal scalability frameworks. In massive distributed networks, local memory buffers are simply insufficient.",
            "We must look at decentralized data caches, network replication latencies, and fault-tolerant computing groups to ensure high availability under extreme traffic requests.",
            "When a node goes offline in a distributed network cluster, the consensus protocol must rapidly re-elect a primary leader without halting current transactional throughput or dropping in-flight user data frames.",
            "In conclusion, whether you are dealing with low-level kernel synchronization locks or high-level cloud architecture maps, managing shared state variables safely is the ultimate engineering hurdle. Make sure to review the upcoming practical assignment guidelines on the portal before tomorrow morning's lab session."
        ]
        english_transcript=[]
        translated_transcript=[]

        try:
            language_code=language_codes.get(target_language,target_language)
            for index, segment in enumerate(lecture_content):
                translated_segment= GoogleTranslator(source='auto', target=language_code).translate(segment)
                english_transcript.append(f"[{index+1}] {segment}")
                translated_transcript.append(f"[{index+1}] {translated_segment}")

            full_english = "\n\n".join(english_transcript)
            full_translated="\n\n".join(translated_transcript)

            return jsonify({
                "success": True,
                "filename": media_file.filename,
                "english_text": full_english,
                "translated_text": full_translated
            })
        except Exception as error:
            return jsonify({"error": f"Translation failed: {str(error)}"}), 500


@app.route('/check_server', methods=['GET'])
def check_server():
    return jsonify({
        "status": "online",
        "version": "1.0.0",
        "is_broadcasting": lecture_data["is_broadcasting"]
    })

if __name__ =='__main__':
    print("==========================================================")
    print(" UWC AI Lecture Translation Server")
    print(" Server URL: http://127.0.0.1:5000")
    print("==========================================================")
    print("The server is now running...")
    app.run(debug=True, host='0.0.0.0',port=5000)