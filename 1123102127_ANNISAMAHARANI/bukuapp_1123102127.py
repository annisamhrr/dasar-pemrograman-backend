from flask import Flask, render_template, request, redirect, url_for, jsonify
import pymysql

app = Flask(__name__)

# Fungsi untuk mengatur koneksi database
def get_db_connection():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="icha",
            database="perpus_1123102127",
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn
    except Exception as e:
        raise Exception(f"Gagal terhubung ke database: {e}")

# Endpoint API untuk mendapatkan semua buku (GET)
@app.route("/api/buku", methods=["GET"])
def get_all_buku():
    conn = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM buku_1123102127")
            books = cursor.fetchall()
        return jsonify({"status": "success", "data": books}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        if conn:
            conn.close()

# Endpoint API untuk mendapatkan buku by ID (GET)
@app.route("/api/buku/<int:id>", methods=["GET"])
def get_buku_by_id(id):
    conn = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM buku_1123102127 WHERE Kode_Buku=%s", (id,))
            book = cursor.fetchone()
            if book:
                return jsonify({"status": "success", "data": book}), 200
            return jsonify({"status": "error", "message": "Buku tidak ditemukan"}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        if conn:
            conn.close()

# Endpoint API untuk menambah buku (POST)
@app.route("/tambah", methods=["GET", "POST"])
def tambah():
    conn = None
    try:
        if request.method == "POST":
            # Ambil data dari form
            kode_buku = request.form["kode_buku"]
            nama_buku = request.form["nama_buku"]
            penerbit = request.form["penerbit"]
            pengarang = request.form["pengarang"]
            jumlah_buku = request.form["jumlah_buku"]

            # Validasi data
            if not kode_buku or not nama_buku or not penerbit or not pengarang or not jumlah_buku:
                return "Semua field harus diisi!", 400

            # Simpan ke database
            conn = get_db_connection()
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO buku_1123102127 (Kode_Buku, Nama_Buku, Penerbit, Pengarang, Jumlah_Buku) VALUES (%s, %s, %s, %s, %s)",
                    (kode_buku, nama_buku, penerbit, pengarang, jumlah_buku),
                )
            conn.commit()
            return redirect(url_for("index"))  # Redirect ke halaman utama setelah berhasil menambah buku

        # Jika GET, tampilkan form tambah buku
        return render_template("tambah_1123102127.html")
    except Exception as e:
        return f"Terjadi kesalahan: {e}"
    finally:
        if conn:
            conn.close()

# Endpoint API untuk update buku (PUT)
@app.route("/api/buku/<int:id>", methods=["PUT"])
def update_buku(id):
    conn = None
    try:
        if request.headers.get('Content-Type') != 'application/json':
            return jsonify({"status": "error", "message": "Content-Type harus application/json"}), 400

        data = request.get_json()
        required_fields = ["Nama_Buku", "Penerbit", "Pengarang", "Jumlah_Buku"]
        for field in required_fields:
            if field not in data:
                return jsonify({"status": "error", "message": f"Field {field} harus diisi"}), 400

        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM buku_1123102127 WHERE Kode_Buku=%s", (id,))
            if not cursor.fetchone():
                return jsonify({"status": "error", "message": "Buku tidak ditemukan"}), 404

            cursor.execute(
                "UPDATE buku_1123102127 SET Nama_Buku=%s, Penerbit=%s, Pengarang=%s, Jumlah_Buku=%s WHERE Kode_Buku=%s",
                (data["Nama_Buku"], data["Penerbit"], data["Pengarang"], data["Jumlah_Buku"], id)
            )
        conn.commit()
        return jsonify({"status": "success", "message": "Buku berhasil diupdate"}), 200
    except Exception as e:
        if conn:
            conn.rollback()
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        if conn:
            conn.close()

# Route untuk menampilkan semua buku di web interface
@app.route("/")
def index():
    conn = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM buku_1123102127")
            books = cursor.fetchall()
        return render_template("index_1123102127.html", buku=books)
    except Exception as e:
        return f"Terjadi kesalahan: {e}"
    finally:
        if conn:
            conn.close()

# Jalankan server
if __name__ == "__main__":
    app.run(debug=True)
