# First Flask Project - Pertemuan 11

Projek sederhana Python Flask mencakup materi dasar routing hingga penanganan form dengan method POST dan Jinja2 template.

## Fitur & Materi
1. **Routing Dasar & Dynamic URLs**: Routing string `<name>` dan integer `<int:post_id>`.
2. **Template Jinja2**: Rendering template HTML dengan parsing variabel (`hello.html`, `greet.html`).
3. **Form Handling (POST)**: Form input dengan TextField, Label, dan Button untuk mengirim data via method POST (`index.html`).
4. **Styling CSS**: Menggunakan CSS statis dari folder `static/styles.css`.

## Struktur Direktori
```text
.
├── .gitignore
├── Introduction to Flask.pptx
├── README.md
└── Teori/
    ├── app.py
    ├── static/
    │   └── styles.css
    └── templates/
        ├── greet.html
        ├── hello.html
        └── index.html
```

## Cara Menjalankan
1. Pastikan Flask sudah terinstal:
   ```bash
   pip install flask
   ```

2. Jalankan aplikasi:
   ```bash
   flask --app Teori/app run --debug
   ```
   atau
   ```bash
   python Teori/app.py
   ```

3. Akses form tugas POST:
   Buka browser dan buka `http://127.0.0.1:5000/tugas`
