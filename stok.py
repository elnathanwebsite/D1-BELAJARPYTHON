from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/products', methods=['GET'])
def get_products():
    products = [
        {
            "id": 1,
            "nama": "Produk A",
            "kategori": "Elektronik",
            "harga": 250000,
            "stok": 10,
            "gambar": "https://via.placeholder.com/100",  # Link gambar
            "link_pembayaran": "https://www.example.com/beli-produk-a"  # Link pembayaran
        },
        {
            "id": 2,
            "nama": "Produk B",
            "kategori": "Pakaian",
            "harga": 100000,
            "stok": 20,
            "gambar": "https://via.placeholder.com/100",  # Link gambar
            "link_pembayaran": "https://www.example.com/beli-produk-b"  # Link pembayaran
        }
    ]
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
