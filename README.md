Implementasi Abstractive Text Summarization Berbasis Indo-T5 🇮🇩

Repository ini berisi kode sumber untuk Tugas Akhir (Final Project) dengan topik Peringkasan Teks Otomatis (Abstractive Text Summarization) pada artikel berita Bahasa Indonesia menggunakan pendekatan Deep Learning.

📖 Deskripsi Proyek

Proyek ini bertujuan untuk membangun sistem yang mampu membaca artikel berita panjang dan menghasilkan ringkasan pendek yang akurat dan koheren secara otomatis.

Metode yang digunakan:

Model: Indo-T5 (Transfer Learning dari T5-Base Indonesian).

Dataset: 5.000 Artikel Berita Liputan6 (Hasil Scraping & Cleaning).

Framework: PyTorch & Hugging Face Transformers.

Interface: Flask Web Framework.

⚠️ PENTING: Download Model Pre-Trained

Karena ukuran file model (pytorch_model.bin) sangat besar (>800 MB), file model TIDAK DISIMPAN di repository GitHub ini.

Untuk menjalankan aplikasi ini, Anda wajib mengunduh model yang sudah dilatih (Fine-tuned) melalui link berikut:

👉 DOWNLOAD MODEL (GOOGLE DRIVE)
https://drive.google.com/drive/folders/1g2fcMAHE7NXxCmpTA16xGx-rTrXBVxeP?usp=drive_link

Cara Pemasangan Model:

Klik link di atas.

Download folder/file model tersebut.

Ekstrak (Unzip) jika dalam bentuk zip.

Letakkan file-file model di dalam folder bernama model_final di direktori utama proyek ini.

Struktur folder harus terlihat seperti ini:

Project_Ini/
├── app.py
├── templates/
├── model_final/          <-- TARUH HASIL DOWNLOAD DI SINI
│   ├── config.json
│   ├── pytorch_model.bin
│   ├── tokenizer.json
│   └── ...
└── ...


⚙️ Instalasi & Persiapan

Pastikan Anda sudah menginstall Python di komputer Anda.

Clone Repository ini:

git clone [https://github.com/username-anda/repo-anda.git](https://github.com/username-anda/repo-anda.git)
cd repo-anda


Install Library yang Dibutuhkan:
Disarankan menggunakan virtual environment. Install dependencies dengan perintah:

pip install flask transformers torch


🚀 Cara Menjalankan Aplikasi Web

Setelah model di-download dan library di-install:

Buka terminal/CMD di folder proyek.

Jalankan perintah:

python app.py


Tunggu hingga muncul pesan Running on http://127.0.0.1:5000.

Buka browser dan akses alamat tersebut.

Masukkan teks berita panjang, lalu klik Ringkas Sekarang.

📊 Hasil Evaluasi Model

Model ini telah dilatih selama 3 Epoch pada 5.000 data latih. Berikut adalah hasil evaluasi menggunakan metrik ROUGE:

Metrik

Skor (%)

Deskripsi

ROUGE-1

39.82%

Tingkat kecocokan kata (unigram) dengan ringkasan manusia.

ROUGE-2

21.89%

Tingkat kecocokan frasa (bigram) dan kelancaran teks.

ROUGE-L

33.03%

Tingkat kesamaan struktur kalimat (Longest Common Subsequence).

Hasil ini menunjukkan peningkatan signifikan dibandingkan metode baseline (BERT-Extractive).

📂 Struktur Folder

app.py: File utama backend (Flask) untuk menjalankan server.

templates/: Berisi file HTML (index.html) untuk tampilan antarmuka web.

preprocessing_scripts/ (Opsional): Skrip yang digunakan untuk scraping dan pembersihan data.

model_final/: (Diabaikan oleh Git) Tempat menyimpan model hasil training.

Credits

Dataset asli merujuk pada Liputan6 Summarization Corpus.
Base Model menggunakan cahya/t5-base-indonesian-summarization-cased.

Dibuat oleh: [Nama Anda/Kelompok Anda] - Mahasiswa Semester 7