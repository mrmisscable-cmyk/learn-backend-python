from flask import Flask, jsonify, request

# 1. Inisialisasi aplikasi Flask
app = Flask(__name__)

# 2. Route Pertama: Halaman Utama (Home)
@app.route("/")
def home():
    return "Halo, Mochammad Hanafi! Server Flask-mu sudah aktif dan berjalan dengan sukses. 🚀"

# 3. Route Kedua: Halaman Tentang (About)
@app.route("/about")
def about():
    return "Ini adalah halaman tentang web backend pertamaku menggunakan Flask."

# 4. Route Ketiga: Dynamic Routing (Menerima parameter dari URL)
# Contoh: http://localhost:5000/sapa/Hanafi
@app.route("/sapa/<nama>/<asal>")
def sapa_user(nama, asal):
    return f"Halo {nama} asal {asal}! Senang berkenalan denganmu di backend Python."

# 5. Route Keempat: Menerima data Query Parameter (Contoh: /cari?keyword=flask)
@app.route("/cari")
def cari_data():
    # Mengambil nilai dari URL, contoh: /cari?keyword=python
    keyword = request.args.get("keyword", "Tidak ada kata kunci")
    return f"Kamu sedang mencari data dengan kata kunci: <b>{keyword}</b>"

# 6. Menjalankan Server Lokal
if __name__ == "__main__":
    # debug=True artinya server akan otomatis merestart jika kodenya kita ubah dan simpan
    app.run(debug=True, port=5000)