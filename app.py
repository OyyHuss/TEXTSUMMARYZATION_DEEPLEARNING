from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

app = Flask(__name__)

# --- CONFIG ---
# Arahkan ke folder tempat Anda menaruh file model hasil download
MODEL_PATH = "./model_final" 

print(f"Sedang memuat model dari {MODEL_PATH}...")
try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)
    print("✅ Model Berhasil Dimuat di Laptop!")
except Exception as e:
    print(f"❌ Gagal memuat model. Pastikan folder '{MODEL_PATH}' berisi file model lengkap.")
    print(f"Error: {e}")

def ringkas_teks(teks):
    input_text = "summarize: " + teks
    # Di laptop biasanya tidak ada GPU Nvidia, jadi otomatis pakai CPU (lebih lambat tapi pasti jalan)
    inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)
    
    outputs = model.generate(
        inputs["input_ids"], 
        max_length=128, 
        min_length=30, 
        length_penalty=2.0, 
        num_beams=4, 
        early_stopping=True
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

@app.route('/', methods=['GET', 'POST'])
def home():
    summary = ""
    original_text = ""
    if request.method == 'POST':
        original_text = request.form['berita']
        if original_text:
            summary = ringkas_teks(original_text)
    return render_template('index.html', summary=summary, original_text=original_text)

if __name__ == '__main__':
    app.run(debug=True)